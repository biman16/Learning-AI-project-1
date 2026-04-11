from transformers import pipeline

classifier = pipeline("image-classification")

results = classifier("cat.jpeg")

print("\nImage Classification result: \n")

for r in results:
    print(f"Label: {r['label']},  Score: {round(r['score'], 4)}")