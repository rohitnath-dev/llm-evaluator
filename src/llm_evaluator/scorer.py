def normalize_text(text: str) -> str:
  text = text.strip()
  text = text.lower()

  return text


def score_answer(model_answer, ideal):
  model_answer = normalize_text(model_answer)
  score = 0.0

  if isinstance(ideal, list):
    for ans in ideal:
      ans = normalize_text(ans)

      if model_answer == ans:
        score = 1.0
        break

  else:
    ideal = normalize_text(ideal)

    if ideal == model_answer:
      score = 1.0

  return score