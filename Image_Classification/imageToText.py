from transformers import pipeline

imageToText = pipeline("image-to-text")

result = imageToText("cat.jpeg")

print(f"Text: {result[0]['generated_text']}")