import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from agents.contract_agent import find_contract_info
from agents.payment_agent import answer_payment_query  # 🔹 入金エージェントを追加

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

def handle_user_query(user_input: str) -> str:
    user_input_lower = user_input.lower()

    # 🔹 payment系の質問かどうかを判定
    if "payment" in user_input_lower or "paid" in user_input_lower or "pay" in user_input_lower:
        print("🪙 Routed to payment_agent")  # ← ここを追加
        payment_info = answer_payment_query(user_input)
        return payment_info

    # 🔹 それ以外は契約情報と判断
    print("📄 Routed to contract_agent")  # ← ここを追加
    retrieved_info = find_contract_info(user_input)

    prompt = f"""
You are a helpful assistant for rental property management.

Here is the information retrieved from the contract database:
{retrieved_info}

Based on this data, please answer the user's question:
"{user_input}"

If the data is not sufficient to answer, say "I'm sorry, I couldn't find a match."
"""

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=deployment,
        temperature=0,
        max_tokens=1000,
        top_p=1.0,
    )

    return response.choices[0].message.content.strip()