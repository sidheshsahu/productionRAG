from deepeval.models import GeminiModel
from deepeval.metrics import AnswerRelevancyMetric

model = GeminiModel(
    model="gemini-2.5-pro",
    api_key=os.getenv('GOOGLE_API_KEY'),
    temperature=0,
)

answer_relevancy = AnswerRelevancyMetric(model=model)