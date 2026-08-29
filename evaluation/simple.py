from deepeval.models import GeminiModel
from deepeval.metrics import AnswerRelevancyMetric
import os
from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.evaluate import AsyncConfig
from deepeval.metrics import AnswerRelevancyMetric
from evaluation.q_and_a_list import questions,pred_ans
import time

model = GeminiModel(
    model="gemini-3.7-flash",
    
    api_key=os.getenv('GOOGLE_API_KEY'),
    temperature=0.4,
)

metric = AnswerRelevancyMetric(
threshold=0.7,
model=model,
include_reason=True
)

results = []

for i, (question, pred_ans) in enumerate(zip(questions, pred_ans)):

    test_case = LLMTestCase(
        input=question,
        actual_output=pred_ans,
    )

    result = evaluate(
        test_cases=[test_case],
        metrics=[metric],
    )

    results.append(result)

    print(f"Completed {i + 1}/{len(questions)}:", question) 
    
