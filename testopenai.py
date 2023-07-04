import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]


completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k-0613", messages=[{"role": "user", "content": "介绍一下广州塔"}]
)
print(completion.choices[0].message.content)
