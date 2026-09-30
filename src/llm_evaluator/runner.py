from typing import Protocol


class Model(Protocol):
  def generate(self, messages: list[dict[str, str]]) -> str:
    ...


def run_model(model: Model, messages: list[dict[str, str]]) -> str:
  return model.generate(messages)


class HuggingFaceModel:
  def __init__(self, model_name: str, **kwargs):
    from transformers import pipeline

    self.model = pipeline(
      "text-generation",
      model=model_name,
      **kwargs
    )

  def generate(self, messages: list[dict[str, str]]) -> str:
    response = self.model(
      messages,
      max_new_tokens=256,
      return_full_text=False
    )

    return response[0]["generated_text"]