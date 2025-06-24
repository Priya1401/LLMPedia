system_prompt = (
    "You are an assistant that takes a raw meeting transcript and "
    "produces clear, action-oriented meeting minutes in Markdown. "
    "Include sections for:\n"
    "1. Key Discussion Points\n"
    "2. Key Takeaways\n"
    "3. Action Items (with owners)\n"
)

def get_minutes_user_prompt(transcript: str) -> str:
    return (
        "Here is the transcript of a meeting:\n\n"
        "```text\n"
        f"{transcript}\n"
        "```\n\n"
        "Please generate meeting minutes as described."
    )
