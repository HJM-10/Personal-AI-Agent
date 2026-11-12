# Huzaifa Jayyad Mirza · Digital Clone

This is an AI clone, not the real person.

## Knowledge base

The six Markdown documents are based on Huzaifa's personal accounts. The bio and FAQ cover factual details and his voice. The Light CI/CD and Spend Trial write-ups distinguish completed work from future plans. The interests and UMT advice pieces cover opinions and longer first-person experiences.

## Retrieval and evaluation

The app indexed 17 overlapping chunks. BM25 matches exact words, while dense retrieval compares BGE sentence embeddings with cosine similarity. Hybrid uses Reciprocal Rank Fusion with a constant of 60. Weighted fusion would instead normalize the two sets of scores and blend them using a tunable weight.

| Question | BM25 | Dense | Hybrid | Best mode and why |
| --- | --- | --- | --- | --- |
| What did I implement with Nixpacks? | faq:2, faq:6, faq:1 | projects:1, faq:7, faq:6 | faq:6, projects:1, faq:7 | Dense. The first passage describes the owner's implementation directly. |
| Academic transition surprises? | No hits | bio:2, umt-student-advice:1, faq:3 | bio:2, umt-student-advice:1, faq:3 | Dense and Hybrid tie. The relevant assessment stories appear at ranks two and three. |
| What made me build Spend Trial? | spend-trial:1, umt-student-advice:2, faq:5 | spend-trial:1, umt-student-advice:2, faq:5 | spend-trial:1, umt-student-advice:2, faq:5 | Tie. The top passage explains the budgeting problem. |
| Why do I enjoy Cyber Forensics? | technology-interests:1, faq:3, faq:4 | technology-interests:1, faq:4, faq:3 | technology-interests:1, faq:3, faq:4 | Tie at rank one. The interests piece explains the appeal of reconstructing incidents. |
| What's my favorite restaurant? | bio:1, faq:3, technology-interests:1 | technology-interests:1, faq:2, bio:2 | technology-interests:1, bio:2, faq:3 | No mode found supporting evidence. The intended answer is the fallback. |

The table lists the top three chunk IDs in order, with `.md` omitted. The paraphrase shares zero words with the answer to FAQ 8. A retrieval failure occurred on the restaurant question. All modes returned unrelated passages because a ranking can still surface the best available results when the corpus contains no answer. The generation prompt instructs the model to abstain in this situation. Live generation still needs to be checked after setting the deployment secret.

One improvement would be to label supporting passages for a larger set of questions and track hit@3 as the corpus changes.

## Run locally

```sh
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

Run `python app.py` to use the Gradio interface. The repo includes the precomputed embeddings. After changing the documents, run `python retrieval.py` to rebuild the index.

## Deploy on Streamlit Community Cloud

Select this repository, branch `main`, and main file `streamlit_app.py`. Use Python 3.12 in Advanced settings. Add a top-level secret named `HF_TOKEN` with permission to call Hugging Face Inference Providers. The default model is `Qwen/Qwen2.5-7B-Instruct`. Set the optional `HF_CHAT_MODEL` variable to use a different model.
