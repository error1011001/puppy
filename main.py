import os
import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = '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'
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})