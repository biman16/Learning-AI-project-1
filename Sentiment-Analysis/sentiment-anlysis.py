from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis")

sentences = [
     "I love this product, it's amazing!",
    "This is the worst experience ever.",
    "The movie was okay, not great but not bad."
]

for sentence in sentences:
    result = sentiment_analysis(sentence)[0]

    print("\nSentece: ", sentence)
    print("Sentiment: ", result['label'])
    print("Confidence: ", result['score'])