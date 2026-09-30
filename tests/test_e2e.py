import random
from pathlib import Path

from llm_evaluator import (
  HuggingFaceModel,
  load_dataset,
  evaluate_samples
)


DATA_DIR = Path("data")
NUM_SAMPLES = 5


all_samples = []

for file in DATA_DIR.glob("*.jsonl"):
  samples = load_dataset(file)
  all_samples.extend(samples)


samples = random.sample(
  all_samples,
  min(NUM_SAMPLES, len(all_samples))
)

model = HuggingFaceModel(
  "Qwen/Qwen2.5-0.5B-Instruct"
)

report = evaluate_samples(
  model,
  samples
)

print("\nEvaluation Results")
print("------------------")

for result in report.results:
  print(f"\nSample: {result.sample_id}")
  print(f"Model answer: {result.model_answer}")
  print(f"Score: {result.score}")

print("\nSummary")
print("-------")
print("Total samples:", report.total_samples)
print("Average score:", report.average_score)