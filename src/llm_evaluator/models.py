from dataclasses import dataclass
from typing import Any


@dataclass
class EvaluationSample:
  id: str
  input: list[dict[str, str]]
  ideal: Any


@dataclass
class EvaluationResult:
  sample_id: str
  model_answer: str
  score: float


@dataclass
class EvaluationReport:
  total_samples: int
  average_score: float
  results: list[EvaluationResult]