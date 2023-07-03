import openai

openai.api_key = "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"  # 将第二步获取的密钥填写到这里


completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k-0613", messages=[{"role": "user", "content": "介绍一下广州塔"}]
)
print(completion.choices[0].message.content)
