import os
from dotenv import load_dotenv
from azure.cosmos import CosmosClient

load_dotenv()

COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
COSMOS_KEY = os.getenv("COSMOS_KEY")
COSMOS_DB = os.getenv("COSMOS_DB")
COSMOS_CONTAINER_CONTRACTS = os.getenv("COSMOS_CONTAINER_CONTRACTS")
COSMOS_CONTAINER_PAYMENTS = os.getenv("COSMOS_CONTAINER_PAYMENTS")

client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
db = client.get_database_client(COSMOS_DB)
contracts_container = db.get_container_client(COSMOS_CONTAINER_CONTRACTS)
payments_container = db.get_container_client(COSMOS_CONTAINER_PAYMENTS)

def get_all_contracts():
    try:
        return list(contracts_container.read_all_items())
    except Exception as e:
        print(f"Error fetching contracts: {e}")
        return []

def get_all_payments():
    try:
        return list(payments_container.read_all_items())
    except Exception as e:
        print(f"Error fetching payments: {e}")
        return []

def add_contract(contract_info):
    try:
        response = contracts_container.create_item(body=contract_info)
        return response
    except Exception as e:
        print(f"Error adding contract: {e}")
        return None

def update_contract_last_payment(name: str, payment_date: str):
    query = "SELECT * FROM c WHERE LOWER(c.name) = @name"
    params = [{"name": "@name", "value": name.lower()}]
    contracts = list(contracts_container.query_items(query=query, parameters=params, enable_cross_partition_query=True))

    if not contracts:
        return False

    contract = contracts[0]
    contract["last_payment_date"] = payment_date

    contracts_container.upsert_item(contract)
    return True