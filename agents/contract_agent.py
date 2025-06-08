import os
from services.cosmos_client import get_all_contracts
from dotenv import load_dotenv

load_dotenv()

def find_contract_info(user_input: str) -> str:
    contracts = get_all_contracts()

    # ユーザー入力を小文字で比較
    input_lower = user_input.lower()

    # マッチする契約情報を探す
    for contract in contracts:
        name = contract.get("name", "").lower()
        property_name = contract.get("property_name", "").lower()

        # 入力に氏名や物件名が含まれていたら返す
        if name in input_lower or property_name in input_lower:
            return f"{contract.get('name')} lives at {contract.get('property_name')} and pays {contract.get('amount')} yen in rent."

    return "Sorry, I couldn't find any matching contract data based on your question."