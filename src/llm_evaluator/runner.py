from transformers import pipeline


class HuggingFaceModel:
  def __init__(self, model_name):
    self.model = pipeline(
      "text-generation",
      model=model_name
    )

  def generate(self, messages):
    response = self.model(
      messages,
      max_new_tokens=256,
      return_full_text=False
    )

    return response[0]["generated_text"]


def run_model(model, messages):
  response = model.generate(messages)

  return response