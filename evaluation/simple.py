from deepeval.models import GeminiModel
from deepeval.metrics import AnswerRelevancyMetric
import os
from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from evaluation.q_and_a_list import questions,pred_ans


model = GeminiModel(
    model="gemini-3.6-flash",
    
    api_key=os.getenv('GOOGLE_API_KEY'),
    temperature=0.4,
)


metric = AnswerRelevancyMetric(
threshold=0.7,
async_mode=False,
model=model,
include_reason=True
)

print("ASYNC MODE:", metric.async_mode)

test_cases = []

for question, pred_ans in zip(questions, pred_ans):
    test_case = LLMTestCase(
        input=question,
        actual_output=pred_ans,
    )

    test_cases.append(test_case)

# Evaluate all test cases
results = evaluate(
    test_cases=test_cases,
    metrics=[metric]
)


