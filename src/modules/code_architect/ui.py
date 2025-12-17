import streamlit as st
from .generator import architect_review

def code_architect_tab(client, model_name):
    st.header("🏗️ Code Architect")
    st.write("Submit your code snippet for a professional architectural review and optimization.")

    code_input = st.text_area("Paste your code here:", height=300)
    
    if st.button("Review Code"):
        if not code_input.strip():
            st.warning("Please paste some code first.")
        else:
            with st.spinner("Analyzing architecture and code quality..."):
                try:
                    review = architect_review(client, model_name, code_input)
                    st.markdown(review)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
