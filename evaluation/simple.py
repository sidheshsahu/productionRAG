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
    model="gemini-3.6-flash",
    
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
    
    if i < len(questions) - 1: 
        print("Waiting 60 seconds before next question...") 
        time.sleep(60)

# test_cases = []

# for question, pred_ans in zip(questions, pred_ans):
#     test_case = LLMTestCase(
#         input=question,
#         actual_output=pred_ans,
#     )

#     test_cases.append(test_case)

# # Evaluate all test cases
# results = evaluate(
#     test_cases=test_cases,
#     metrics=[metric],
#     async_config=AsyncConfig(
#         run_async=False
#     )
# )


