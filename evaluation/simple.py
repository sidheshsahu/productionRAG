from deepeval.models import GeminiModel
from deepeval.metrics import AnswerRelevancyMetric
import os
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric

model = GeminiModel(
    model="gemini-3.6-flash",
    api_key=os.getenv('GOOGLE_API_KEY'),
    temperature=0.4,
)

answer_relevancy_metric = AnswerRelevancyMetric(model=model)
test_case = LLMTestCase(
  input="Who is the current president of the United States of America?",
  actual_output="Joe Biden",
  retrieval_context=["Joe Biden serves as the current president of America."]
)
answer_relevancy_metric.measure(test_case)
print(answer_relevancy_metric.score)


