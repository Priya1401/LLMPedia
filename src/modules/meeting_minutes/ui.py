import streamlit as st
from .generator import create_minutes, stream_minutes

def meeting_minutes_tab(client, model_name):
    st.header("Meeting Minutes Summarizer")
    st.write("Upload an audio file (mp3/m4a/wav) and get back markdown-formatted minutes.")

    audio = st.file_uploader("Upload meeting audio", type=["mp3","m4a","wav"])
    if not audio:
        st.info("Please upload an audio file to proceed.")
        return

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Generate Minutes"):
                with st.spinner("Processing audio..."):
                    try:
                        minutes = create_minutes(client, model_name, audio)
                        st.markdown(minutes)
                    except Exception as e:
                        st.error(f"Error: {e}")
        
        if st.button("Generate (Stream)"):
            st.write("---")
            stream_container = st.empty()
            def update_stream(text):
                stream_container.markdown(text)
            
            try:
                stream_minutes(client, model_name, audio, update_stream)
            except Exception as e:
                 st.error(f"Error: {e}")
