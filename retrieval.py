"""Build and query the local hybrid search index."""

import hashlib
import json
import re
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

ROOT = Path(__file__).resolve().parent
MODEL = "BAAI/bge-small-en-v1.5"
MODEL_REVISION = "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
EMBEDDINGS = ROOT / "embeddings.npy"
FINGERPRINT = ROOT / "embeddings.sha256"
MODES = ("BM25 only", "Dense only", "Hybrid")


@dataclass(frozen=True)
class Chunk:
    source: str
    id: str
    text: str


def load_chunks():
    chunks = []
    for path in sorted((ROOT / "data").iterdir()):
        if path.suffix.lower() not in {".md", ".txt"}:
            continue
        words = path.read_text(encoding="utf-8-sig").split()
        start = 0
        number = 1
        while start < len(words):
            end = min(start + 250, len(words))
            if len(words) - end < 50:
                end = len(words)
            chunks.append(Chunk(path.name, f"{path.name}:{number}", " ".join(words[start:end])))
            if end == len(words):
                break
            start = end - 40
            number += 1
    if not chunks:
        raise ValueError("Add a Markdown or text document under data/.")
    return chunks


def fingerprint(chunks):
    payload = json.dumps([MODEL, MODEL_REVISION, [asdict(chunk) for chunk in chunks]], ensure_ascii=False)
    return hashlib.sha256(payload.encode()).hexdigest()


def tokenize(text):
    return re.findall(r"\w+", text.casefold())


class Retriever:
    def __init__(self):
        self.chunks = load_chunks()
        if not FINGERPRINT.exists() or FINGERPRINT.read_text().strip() != fingerprint(self.chunks):
            raise ValueError("Run python retrieval.py to build embeddings for the current documents.")
        self.embeddings = np.load(EMBEDDINGS, allow_pickle=False)
        if self.embeddings.shape != (len(self.chunks), 384):
            raise ValueError("Embedding dimensions do not match the corpus. Run python retrieval.py.")
        self.encoder = SentenceTransformer(MODEL, revision=MODEL_REVISION, device="cpu")
        self.tokens = [set(tokenize(chunk.text)) for chunk in self.chunks]
        self.bm25 = BM25Okapi([tokenize(chunk.text) for chunk in self.chunks])

    def rankings(self, question, mode, top_k=3):
        if mode not in MODES:
            raise ValueError(f"Unknown retrieval mode: {mode}")
        rankings = []
        if mode in ("BM25 only", "Hybrid"):
            terms = tokenize(question)
            scores = self.bm25.get_scores(terms)
            hits = [i for i, tokens in enumerate(self.tokens) if tokens.intersection(terms)]
            rankings.append(sorted(((i, float(scores[i])) for i in hits), key=lambda hit: -hit[1]))
        if mode in ("Dense only", "Hybrid"):
            vector = self.encoder.encode(QUERY_PREFIX + question, normalize_embeddings=True)
            scores = self.embeddings @ vector
            order = np.argsort(-scores, kind="stable")
            rankings.append([(int(i), float(scores[i])) for i in order])
        if mode == "Hybrid":
            fused = defaultdict(float)
            for ranking in rankings:
                for rank, (index, _) in enumerate(ranking[:10], start=1):
                    fused[index] += 1 / (60 + rank)
            hits = sorted(fused.items(), key=lambda hit: (-hit[1], hit[0]))
        else:
            hits = rankings[0]
        return [(self.chunks[index], score) for index, score in hits[:top_k]]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        chunks = load_chunks()
        encoder = SentenceTransformer(MODEL, revision=MODEL_REVISION, device="cpu")
        vectors = encoder.encode([chunk.text for chunk in chunks], normalize_embeddings=True)
        np.save(EMBEDDINGS, vectors, allow_pickle=False)
        FINGERPRINT.write_text(fingerprint(chunks) + "\n")
        print(f"Saved {len(chunks)} embeddings.")
    else:
        retriever = Retriever()
        for question in sys.argv[1:]:
            print(question)
            for mode in MODES:
                print(mode, [(chunk.id, round(score, 4)) for chunk, score in retriever.rankings(question, mode)])
