# llm-evaluator

A lightweight, model-agnostic library for evaluating LLMs using curated datasets.

## Features

- JSONL-based evaluation datasets
- Exact-match scoring
- Multiple acceptable answers
- Custom model support
- Hugging Face integration

## Installation

```bash
git clone https://github.com/rohitnath-dev/llm-evaluator.git
cd llm-evaluator
pip install -e .
```

## Usage

```python
from llm_evaluator import load_dataset, evaluate_samples

samples = load_dataset("data/math.jsonl")
report = evaluate_samples(model, samples)

print(report.average_score)
```

Your model only needs to provide:

```
generate(messages) → response
```

## Structure

```
data/     → Evaluation datasets
src/      → Core library
tests/    → Tests
```

## License

MIT
