from transformers import pipeline

from PIL import Image

classifier = pipeline("image-classification")

image = Image.open("cat.jpeg")

results = classifier(image)

print("\nImage Classification result: \n")

for r in results:
    print(f"Label: {r['label']},  Score: {round(r['score'], 4)}")