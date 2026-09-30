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