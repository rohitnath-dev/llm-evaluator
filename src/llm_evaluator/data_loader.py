import json
from pathlib import Path

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