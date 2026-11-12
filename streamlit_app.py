"""Streamlit interface for the digital clone."""

import streamlit as st

from clone import MODES, ask

st.set_page_config(page_title="Huzaifa Jayyad Mirza · Digital Clone")
st.title("Huzaifa Jayyad Mirza")
st.info("This is an AI clone, not the real person.")

with st.form("question_form"):
    question = st.text_input("Question", placeholder="What did you build for Light CI/CD?")
    mode = st.radio("Retrieval mode", MODES, index=2, horizontal=True)
    submitted = st.form_submit_button("Ask", type="primary")

if submitted:
    with st.spinner("Searching the notes…"):
        st.session_state.result = ask(question, mode)

if "result" in st.session_state:
    answer, evidence = st.session_state.result
    st.subheader("Answer")
    st.text(answer)
    if evidence:
        with st.expander("Retrieved passages, sources, and scores", expanded=True):
            st.text(evidence)
