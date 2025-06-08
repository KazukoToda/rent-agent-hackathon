# services/query_utils.py

from services.cosmos_client import CosmosDBClient
from datetime import datetime
import os

client = CosmosDBClient()

def get_payment_by_name_and_month(client, name: str, year: int, month: int):
    container_name = "payments"
    query = f"""
    SELECT * FROM c
    WHERE c.name = @name
    AND STARTSWITH(c.payment_date, @datePrefix)
    """
    params = [
        {"name": "@name", "value": name},
        {"name": "@datePrefix", "value": f"{year}-{int(month):02d}"}
    ]
    results = client.query_items(container_name, query, params)
    return results

def get_unpaid_contracts_by_month(client, year:int, month:int):
    # まず全契約を取得
    contracts_container = client.get_container(os.getenv("COSMOS_CONTAINER_CONTRACTS"))
    contracts = list(contracts_container.read_all_items())

    # 次に、当月分の入金記録を取得
    payments_container = client.get_container(os.getenv("COSMOS_CONTAINER_PAYMENTS"))
    prefix = f"{year}-{str(month).zfill(2)}"
    payments = list(payments_container.query_items(
        query="SELECT c.name FROM c WHERE STARTSWITH(c.date, @prefix)",
        parameters=[{"name": "@prefix", "value": prefix}],
        enable_cross_partition_query=True
    ))
    paid_names = {p["name"] for p in payments}

    # 未収者（契約終了していない & 支払いが確認できない）
    unpaid = []
    for c in contracts:
        end_date = c.get("end_date")
        if end_date and end_date < prefix + "-01":
            continue  # 契約終了
        if c["name"] not in paid_names:
            unpaid.append(c)
    return "未収者一覧:\n" + "\n".join([c["name"] for c in unpaid])

def get_advance_payments(client, name: str):
    payments_container = client.get_container(os.getenv("COSMOS_CONTAINER_PAYMENTS"))
    payments = list(payments_container.query_items(
        query="SELECT c.payment_date FROM c WHERE c.name = @name",
        parameters=[{"name": "@name", "value": name}],
        enable_cross_partition_query=True
    ))

    months = sorted({p["payment_date"][:7] for p in payments if "payment_date" in p})
    return months