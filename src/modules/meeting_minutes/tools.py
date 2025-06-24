def transcribe_audio(openai, audio_file, model: str = "whisper-1") -> str:
    """
    Uses OpenAI’s Whisper API to transcribe an uploaded audio file.
    `audio_file` is a file-like object (e.g. Streamlit UploadedFile).
    Returns the raw transcript text.
    """
    resp = openai.audio.transcriptions.create(
        model=model,
        file=audio_file,
        response_format="text"
    )
    return resp  # resp is the transcription string
