# connection_test.py

import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# .envファイルの読み込み
load_dotenv()

# Azure OpenAI クライアントのセットアップ
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# テストメッセージ送信
response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    messages=[{"role": "user", "content": "Azure OpenAIはつながってますか？"}],
    temperature=0
)

# 応答表示
print("✅ 応答:", response.choices[0].message.content.strip())