import os
import openai

# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ["AZURE_API_KEY"]
openai.api_base = os.environ["AZURE_API_BASE"]
openai.api_type = 'azure'
openai.api_version = '2023-05-15'
deployment_name="gpt-35-turbo" # e.g. deployment_name='gpt-35-turbo'

messages = [{"role": "user", "content": "AI是什么"}]
response = openai.ChatCompletion.create(
   engine="chatgpt3516k",
   messages=messages,
   temperature=0,
)
print(response.choices[0].message["content"])
