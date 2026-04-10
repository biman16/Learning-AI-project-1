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

## Tech Used:
- Python
- Transformers (Hugging Face)