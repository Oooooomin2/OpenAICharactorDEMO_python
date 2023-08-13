import openai

openai.api_key = "apikeyを入力"

while(True):
    user_content = input("おれ: ")
    if not user_content:
        break

    messages = [
        {"role": "system", "content": "あなたは不良です。私が言うことに対して全て喧嘩をするような感じで返答してください。"},
        {"role": "user", "content": user_content}
    ]
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    print(f"AIくん: {chat_completion.choices[0].message.content}")