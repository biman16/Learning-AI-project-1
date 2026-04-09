from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompts = [
    "The future of Ai is",
    "Onece upon a time in India, ",
    "In 2050, human will be"
]

tempretures = [0.2, 0.7, 1.2]

for promt in prompts:
    print("\n===================================")
    print("Prompt: ", promt)

    for temp in tempretures:
        print(f"\nTemperature: {temp}")

        result = generator(promt, max_length=40, temperature=temp)

        print(result[0]['generated_text'])






