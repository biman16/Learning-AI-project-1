from transformers import pipeline

summarizer = pipeline("summarization")

text = """
Artificial Intelligence is transforming the world rapidly. It is being used in healthcare to diagnose diseases,
in finance to detect fraud, and in education to personalize learning experiences. AI systems can analyze large
amounts of data quickly and make decisions with high accuracy. However, there are also concerns about job loss,
privacy, and ethical issues. Researchers are working to make AI more transparent and fair.
"""

short_summary = summarizer(
    text,
    max_length=30,
    min_length=10,
    do_sample=False
)

long_summary = summarizer(
    text,
    max_length=80,
    min_length=30,
    do_sample=False
)

print("Short Summary:\n", short_summary[0]["summary_text"])
print("Long Summary:\n", long_summary[0]["summary_text"])
