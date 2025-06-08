from services.cosmos_client import get_all_payments
from datetime import datetime
import re

def answer_payment_query(user_query: str) -> str:
    print(f"📥 Incoming query: {user_query}")

    payments = get_all_payments()
    print(f"📊 Loaded {len(payments)} payment records")

    user_query_lower = user_query.lower()
    print(f"🔍 Normalized query: {user_query_lower}")

    # -------------------------
    # Match: How many payments?
    if "how many" in user_query_lower and "payment" in user_query_lower:
        return f"There are {len(payments)} payment records in the database."

    # -------------------------
    # Match: List all payments
    elif "list" in user_query_lower and "payment" in user_query_lower:
        response_lines = []
        for p in payments:
            line = f"ID: {p.get('payment_id', 'N/A')}, Name: {p.get('name', 'N/A')}, Amount: {p.get('amount', 'N/A')}, Date: {p.get('payment_date', 'N/A')}"
            response_lines.append(line)
        return "\n".join(response_lines)

    # -------------------------
    # Match: Did someone pay in a specific month and year?
    month_map = {
        "jan": "January", "feb": "February", "mar": "March", "apr": "April",
        "may": "May", "jun": "June", "jul": "July", "aug": "August",
        "sep": "September", "oct": "October", "nov": "November", "dec": "December"
    }

    # e.g. Did Nancy pay in Feb 2025?
    month_year_match = re.search(
        r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*[\s,]*(\d{4})",
        user_query_lower
    )
    name_match = re.search(r"did\s+([a-z]+)", user_query_lower)

    print(f"📅 Month/Year match: {month_year_match}")
    print(f"🙍 Name match: {name_match}")

    if month_year_match and name_match:
        abbrev, year = month_year_match.groups()
        month_full = month_map.get(abbrev[:3])  # Expand short month name
        name = name_match.group(1)

        matched = []
        for p in payments:
            payment_name = p.get("name", "").lower()
            payment_date_str = p.get("payment_date", "")

            try:
                payment_date = datetime.strptime(payment_date_str, "%Y-%m-%d")
                payment_month = payment_date.strftime("%B")  # e.g. "March"
                payment_year = payment_date.strftime("%Y")
            except Exception:
                continue  # skip invalid date

            if name in payment_name and payment_month == month_full and payment_year == year:
                matched.append(p)

        if matched:
            return f"Yes, {name.capitalize()} made a payment in {month_full} {year}."
        else:
            return f"No, {name.capitalize()} did not make a payment in {month_full} {year}."

    return "Sorry, I couldn't understand the payment-related question."