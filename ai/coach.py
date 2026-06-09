from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = """
You are a world-class chess coach.

Rules:
- Never immediately reveal answers.
- Ask guiding questions.
- Explain concepts simply.
- Encourage thinking.
- Speak like a human coach.
- Never speak like Stockfish.
"""

def ask_coach(position_fen, move_history, user_message):

    prompt = f"""
Current Position:
{position_fen}

Move History:
{move_history}

Student says:
{user_message}
"""

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":prompt}
        ]
    )

    return response.choices[0].message.content
