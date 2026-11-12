"""Gradio interface for the digital clone."""

import gradio as gr

from clone import MODES, ask


with gr.Blocks(title="Huzaifa Jayyad Mirza · Digital Clone") as demo:
    gr.Markdown("# Huzaifa Jayyad Mirza\n**This is an AI clone, not the real person.**")
    question = gr.Textbox(label="Question", placeholder="What did you build for Lite CICD?")
    mode = gr.Radio(list(MODES), value="Hybrid", label="Retrieval mode")
    submit = gr.Button("Ask", variant="primary")
    answer = gr.Textbox(label="Answer", interactive=False)
    evidence = gr.Textbox(label="Retrieved passages · source and score", lines=12, interactive=False)
    gr.on([submit.click, question.submit], ask, [question, mode], [answer, evidence])


if __name__ == "__main__":
    demo.launch()
