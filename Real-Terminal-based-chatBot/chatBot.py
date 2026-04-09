from transformers import pipeline

chatbot = pipeline("text-generation", model="gpt2")

history = ""

print("ChatBot started, Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    history += f"User: {user_input}\nBot:"

    output = chatbot(
        history,
        max_length = len(history.split()) + 50,
        temperature=0.7,
        truncation=True,          
        pad_token_id=50256
        )

    response = output[0]['generated_text'].split("Bot:")[-1]

    print("Bot:", response.strip())

    history += response + "\n"
    history = history[-500:]