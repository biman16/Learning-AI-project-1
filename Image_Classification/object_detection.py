from transformers import pipeline

objectDetection = pipeline("object-detection")

result = objectDetection("cat.jpeg")

for obj in result:
    print(f"Name: {obj['label']}")
    print(f"Score: {obj['score']}")
    print(f"Bounding Box: {obj['box']}")