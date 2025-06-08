import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()

client = AzureOpenAI(
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

response = client.chat.completions.create(
    stream=True,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful translator.",
        },
        {
            "role": "user",
            "content": "How Can I say Thank you in Japanese, especially in Kansai dialect?",
        }
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    model=deployment,
)

for update in response:
    if update.choices:
        print(update.choices[0].delta.content or "", end="")

client.close()