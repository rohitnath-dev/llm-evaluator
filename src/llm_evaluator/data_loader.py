import json
from pathlib import Path
from importlib.resources import files

from .models import EvaluationSample


def load_dataset(path: str | Path) -> list[EvaluationSample]:
  samples = []

  with open(path, "r", encoding="utf-8") as file:
    for line in file:
      line = line.strip()

      if not line:
        continue

      data = json.loads(line)

      sample = EvaluationSample(
        id=data["id"],
        input=data["input"],
        ideal=data["ideal"]
      )

      samples.append(sample)

  return samples


def load_builtin_dataset(name: str) -> list[EvaluationSample]:
  dataset = files("llm_evaluator").joinpath(
    "data",
    f"{name}.jsonl"
  )

  samples = []

  with dataset.open("r", encoding="utf-8") as file:
    for line in file:
      line = line.strip()

      if not line:
        continue

      data = json.loads(line)

      samples.append(
        EvaluationSample(
          id=data["id"],
          input=data["input"],
          ideal=data["ideal"]
        )
      )

  return samples