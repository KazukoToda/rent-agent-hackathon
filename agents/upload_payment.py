import csv
from services.cosmos_client import payments_container

def upload_payments_from_csv(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            payment_id = row.get("payment_id")
            if not payment_id:
                print("⚠️ Skipping row with missing payment_id.")
                continue

            # Cosmos DBに必要なidフィールドを明示的に追加
            row["id"] = payment_id

            # 重複チェック（すでに存在する場合はスキップ）
            try:
                existing = payments_container.read_item(item=payment_id, partition_key=payment_id)
                print(f"⏭ Skipped duplicate payment: {payment_id}")
                continue
            except Exception:
                # NotFoundなら新規追加を試みる
                pass

            try:
                response = payments_container.create_item(body=row)
                print(f"✅ Uploaded payment: {payment_id}")
            except Exception as e:
                print(f"❌ Error uploading payment {payment_id}: {e}")
                continue

if __name__ == "__main__":
    upload_payments_from_csv("data/payments_dummy.csv")