from .runner import run_model
from .scorer import score_answer
from .models import EvaluationSample, EvaluationResult


def evaluate_sample(model, sample: EvaluationSample) -> EvaluationResult:
  model_answer = run_model(model, sample.input)
  score = score_answer(model_answer, sample.ideal)

  result = EvaluationResult(
    sample_id=sample.id,
    model_answer=model_answer,
    score=score
  )

  return result