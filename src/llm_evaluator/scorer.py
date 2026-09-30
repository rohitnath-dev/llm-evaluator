def normalize_text(text: str) -> str:
  text = str(text).strip()
  text = text.lower()

  return text


def score_answer(model_answer, ideal):
  model_answer = normalize_text(model_answer)

  if isinstance(ideal, list):
    for ans in ideal:
      if model_answer == normalize_text(ans):
        return 1.0

    return 0.0

  if model_answer == normalize_text(ideal):
    return 1.0

  return 0.0