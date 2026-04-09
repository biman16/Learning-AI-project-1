from transformers import pipeline

qa = pipeline(
    "question-answering",
     model="distilbert-base-uncased-distilled-squad"
     )

context = """
Machine Learning is a process of teaching machines by themselves without writing rules and codes explicitly.
Machine learning is widely used in medical field, games, and chatbots.
"""

questions = "What is Machine Learning?"

result = qa(question = questions, context= context)

print("Answer: ", result['answer'])
print("Confidence Score: ", result["score"])