from .models import EvaluationSample, EvaluationResult, EvaluationReport
from .runner import Model, run_model
from .scorer import score_answer


def evaluate_sample(
  model: Model,
  judge_model: Model,
  sample: EvaluationSample
) -> EvaluationResult:

  model_answer = run_model(model, sample.input)

  question = sample.input[-1]["content"]

  score = score_answer(
    judge_model,
    question,
    model_answer,
    sample.ideal
  )

  return EvaluationResult(
    sample_id=sample.id,
    model_answer=model_answer,
    score=score
  )


def evaluate_samples(
  model: Model,
  judge_model: Model,
  samples: list[EvaluationSample]
) -> EvaluationReport:

  results = []

  for sample in samples:
    result = evaluate_sample(
      model,
      judge_model,
      sample
    )

    results.append(result)

  average_score = (
    sum(result.score for result in results) / len(results)
    if results
    else 0.0
  )

  return EvaluationReport(
    total_samples=len(results),
    average_score=average_score,
    results=results
  )