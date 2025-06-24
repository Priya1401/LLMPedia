import streamlit as st
from .generator import create_minutes, stream_minutes

def meeting_minutes_tab(openai, model):
    st.header("Meeting Minutes Summarizer")
    st.write("Upload an audio file (mp3/m4a/wav) and get back markdown-formatted minutes.")

    audio = st.file_uploader("Upload meeting audio", type=["mp3","m4a","wav"])
    if not audio:
        st.info("Please upload an audio file to proceed.")
        return

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Generate Minutes"):
            with st.spinner("Transcribing & Summarizing…"):
                md = create_minutes(openai, model, audio)
                st.markdown(md)

    with col2:
        if st.button("Stream Minutes"):
            placeholder = st.empty()
            with st.spinner("Transcribing & Streaming…"):
                stream_minutes(
                    openai, model, audio,
                    display_fn=lambda txt: placeholder.markdown(txt)
                )
