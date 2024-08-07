from openai import OpenAI

openai = OpenAI(
    api_key='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',
)

def get_gpt_response(user_input):
    message = {
        "role": "user",
        "content": user_input
    }

    response = openai.chat.completions.create(
        messages= [message],
        model= "gpt-3.5-turbo"
    )
    return response.choices[0].message.content

def chat():
    while True:
        user_input = input("You: ")
        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_gpt_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
