import streamlit as st
from .generator import create_brochure, stream_brochure

def brochure_tab(openai, model):
    st.header("Build your Company Brochure")
    company = st.text_input("Company Name")
    url     = st.text_input("Company Website URL", value="https://")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Generate Brochure"):
            if not company or not url:
                st.warning("Enter both name and URL.")
            else:
                with st.spinner("Generating…"):
                    md = create_brochure(openai, model, company, url)
                    st.markdown(md)

    with col2:
        if st.button("Stream Brochure"):
            if not company or not url:
                st.warning("Enter both name and URL.")
            else:
                placeholder = st.empty()
                stream_brochure(
                    openai, model, company, url,
                    display_fn=lambda txt: placeholder.markdown(txt)
                )
