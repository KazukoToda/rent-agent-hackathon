from dotenv import load_dotenv
load_dotenv()

import openai
import os
from services.cosmos_client import get_all_contracts

def generate_unpaid_alert(unpaid_list, year, month):
    """
    Generate an English alert message for unpaid tenants.

    Args:
        unpaid_list (list of dict): List of unpaid tenants, e.g. [{"name": ..., "room": ...}, ...]
        year (int): Target year
        month (int): Target month

    Returns:
        str: English reminder message for unpaid tenants
    """
    tenant_names = ', '.join([u['name'] for u in unpaid_list])
    prompt = (
        f"The following tenants have not paid their rent for {year}-{month:02d}: {tenant_names}. "
        "Please write a polite reminder message in English to notify them about their unpaid rent."
    )

    client = openai.AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        messages=[
            {"role": "system", "content": "You are an assistant for a rental property management company."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()