# 🏠 RentMate - AI-powered Agents App for Real Estate Property Owners

This is a conversational AI-powered Streamlit app designed for property owners to manage rental contracts and payment tracking more efficiently.

✅ Built with **Azure OpenAI (GPT-4o)**, **Cosmos DB**, and **multi-agent orchestration**.

---

## 📌 Problem

Many property owners use Excel to manage tenant contracts and payments, making it difficult to:

- Check who has paid for which month
- Track late payments
- Send reminders efficiently

---

## 🛠️ What This App Does

- 💬 Accepts natural language queries like:
  - "Did Nancy pay for March 2025?"
  - ”Which property does Nancy Muller live?"
- 🤖 Automatically routes queries to the appropriate agent (contract or payment)
- 🧠 Keeps track of the last payment date per tenant
- 🏢 Displays tenant lists grouped by property for easy review

---

**Main Components:**

- `Query Agent`: Understands user questions and delegates to appropriate agents
- `Contract Agent`: Retrieves contract data from Cosmos DB
- `Payment Agent`: Retrieves and analyzes payment history
- `Streamlit`: Provides the web UI
- `Cosmos DB`: Stores contract and payment data

---

## 📽 Demo Video

[![Watch the Demo](https://img.youtube.com/vi/mFaOKOvO1Qk/0.jpg)](https://youtu.be/mFaOKOvO1Qk)

---

## 💡 Future Enhancements

- 📤 Send automated email reminders for unpaid tenants
- 📆 Handle prepayments and deposits more flexibly
- 📱 Mobile app support
- 🔍 Vector-based tenant record search for more robust lookup

---

## 🚀 Tech Stack

| Component         | Description                        |
|------------------|------------------------------------|
| 🧠 GPT-4o         | Natural language understanding     |
| ☁️ Azure Cosmos DB | Scalable document-based database |
| 🔧 Streamlit      | Fast interactive web interface     |
| 🤖 Multi-agent    | Modular query handling by intent   |

---

## 📂 Repository Structure

```bash
.
├── agents/
│   ├── query_agent.py
│   ├── contract_agent.py
│   └── payment_agent.py
├── data/
├── services/
├── streamlit_app.py
├── initialize_project.py
├── test/
├── README.md
├── .gitignore
└── requirements.txt

---