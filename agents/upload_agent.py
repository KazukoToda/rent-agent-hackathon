from services.cosmos_client import add_contract
import csv

def upload_contracts_from_csv(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = row['contract_id']  # ← ここを必ず追加
            result = add_contract(row)
            print(f"Uploaded: {row['contract_id']} -> {result}")

if __name__ == "__main__":
    upload_contracts_from_csv("data/contracts_dummy.csv")