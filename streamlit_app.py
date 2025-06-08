import streamlit as st
import os
from services.cosmos_client import get_all_contracts, get_all_payments
from agents.query_agent import handle_user_query
from openai import AzureOpenAI
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()

# Azure OpenAI クライアントのセットアップ
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

# Streamlitの基本設定
st.set_page_config(page_title="RentMate", page_icon="🏠")
st.title("🏠 RentMate")

# 自然言語質問のセクション
st.markdown("### 🔎 Ask about tenants, contracts or payments in natural language.")

user_input = st.text_area("Enter your question:", "", height=100)
if st.button("Ask Question") and user_input.strip():
    st.markdown("### 💬 Answer :")
    response_text = handle_user_query(user_input)

    if "couldn't find" in response_text.lower() or "no matching" in response_text.lower():
        st.info(response_text)
    else:
        st.success(response_text)

# 契約一覧表示

st.markdown("### 📄 Contract Properties List")

contracts = get_all_contracts()

from collections import defaultdict
import pandas as pd

# 建物ごとに契約をまとめる
grouped = defaultdict(list)

for c in contracts:
    full_property = c.get("property_name", "Unknown")  # 例: "Green Hills 233"
    try:
        # "Green Hills 233" → building = "Green Hills", room = "233"
        parts = full_property.rsplit(" ", 1)
        building = parts[0]
        room_number = parts[1]
    except Exception:
        building = full_property
        room_number = "?"

    grouped[building].append({
        "Room Number": room_number,
        "Tenant": c.get("name", ""),
        "Rent": c.get("amount", "")
    })

# Streamlitで表示
for building, units in grouped.items():
    st.markdown(f"### 🏠 {building}")
    df = pd.DataFrame(units)
    df = df.sort_values("Room Number")  # オプション：部屋番号順
    df.reset_index(drop=True, inplace=True)  # ← これを追加
    st.dataframe(df, hide_index=True)

# 入金一覧表示
st.markdown("### 💰 Payment Records")

payments = get_all_payments()

if not payments:
    st.warning("No payment records found.")
else:
    st.dataframe(
        [
            {
                "Payment ID": p.get("payment_id", ""),
                "Tenant": p.get("name", ""),
                "Year": p.get("year", ""),
                "Month": p.get("month", ""),
                "Amount Paid": p.get("amount", ""),
                "Payment Date": p.get("payment_date", "")
            }
            for p in payments
        ]
    )