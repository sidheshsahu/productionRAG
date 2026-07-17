from deepeval.models import GeminiModel
from deepeval.metrics import AnswerRelevancyMetric

model = GeminiModel(
    model="gemini-2.5-pro",
    api_key="Your Gemini API Key",
    temperature=0,
    cost_per_input_token=0.00000125,
    cost_per_output_token=0.00000500
)

answer_relevancy = AnswerRelevancyMetric(model=model)