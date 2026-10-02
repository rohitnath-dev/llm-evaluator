from .judge import judge_answer


def score_answer(model, question, model_answer, ideal):
    score = judge_answer(
        model,
        question,
        ideal,
        model_answer
    )

    return score