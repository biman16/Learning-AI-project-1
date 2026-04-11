# Learning AI Project

## Projects Included:

# 1. Text Generation
- Uses Hugging Face Transformers
- File: text-generation/main.py

# 2. Question Answering
- Extracts answers from context
- File: question-answering/QandA.py

# 3. Terminal Based Ai Chatbot
- Loop input/output
- Maintain conversation history
- Limit context manually

# 4. Text summarization
- Use pipeline("summarization") from Hugging Face Transformers
- Provide one long input text
- Generate:
- Short summary
- Detailed summary
- Control output using:
- max_length
- min_length
- Compare both summarie

# 5. Sentimental Analysis
- Use pipeline("sentiment-analysis")
- Test with at least 3 different sentences
- Output:
- Sentiment label
- Confidence score
- Compare results for different tones

# 6. NER(Named Entity Recogmition)
- Use pipeline("ner")
- Input a paragraph
- Output:
- Entity names
- Entity types (PERSON, ORG, LOCATION, etc.)
- Group similar entities together

# 7. Image Classification
Goal: Identify what is in an image
Use:

pipeline("image-classification")Input:

2–3 images
Output:

Labels
Confidence scores
Concepts:

CNN / ViT
Feature extraction
Softmax

# 8. Image Captioning
Goal: Generate description of an image
Use:

pipeline("image-to-text")

Input:

1–2 images
Output:

Caption (text)
Concepts:

Vision + Language
Encoder → Decoder
Multimodal models

# 9. Object Detection
Goal: Detect and locate objects
Use:

pipeline("object-detection")Input:

1–2 images
Output:

Object labels
Bounding boxes
Confidence scores
Concepts:

Localization + classification
Bounding boxes
Real-world use cases

## Tech Used:
- Python
- Transformers (Hugging Face)