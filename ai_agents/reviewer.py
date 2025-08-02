
# === ai_agents/reviewer.py ===

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

REVIEW_PROMPT_TEMPLATE = """
You are a professional editor. Review the following rewritten chapter for grammar, tone, and readability.
Make minor improvements if needed, but keep the writer's style intact.

Chapter:
"""

def ai_reviewer_feedback(ai_written_text):
    print("\n>> Reviewing AI-written content...")
    try:
        prompt = REVIEW_PROMPT_TEMPLATE + ai_written_text.strip()

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional text reviewer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.5
        )

        reviewed_text = response['choices'][0]['message']['content'].strip()
        return reviewed_text

    except Exception as e:
        print("[Reviewer Error]", e)
        return "[Error] AI reviewer failed to improve the content."
