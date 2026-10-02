from .judge_prompt import SYSTEM_PROMPT


def judge_answer(model, question, ideal_answer, model_answer):

    user_content = f"""
Question:
{question}

Ideal answer:
{ideal_answer}

Model answer:
{model_answer}
"""

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_content
        }
    ]

    response = model.generate(messages)

    score = float(response.strip())

    if score not in (0.0, 1.0):
        raise ValueError(
            f"Judge returned invalid score: {response}"
        )

    return score