# RentMate

An AI-powered agentic application for rent and subscription payment tracking.

## Overview

RentMate is a modern agentic app built with Azure OpenAI, Azure Cosmos DB, and Azure AI Agents. It automates rent management, payment tracking, and contract operations for property managers.

## Features

- Natural language Q&A about tenants and payment history
- Automated unpaid rent alerts (in English)
- Contract management (renewal, cancellation, CRUD)
- CSV data upload to Cosmos DB
- Retrieval-Augmented Generation (RAG) with Cosmos DB vector search

## Architecture

- **Frontend:** Streamlit (Python)
- **Agents:** Query Agent, Alert Agent, Contract Agent, Upload Agent
- **Database:** Azure Cosmos DB (NoSQL, vector search)
- **AI:** Azure OpenAI (GPT-4o, GPT-3.5-turbo, etc.)

## Directory Structure

```
agents/
  query_agent.py
  alert_agent.py
  contract_agent.py
  upload_agent.py
  cosmos_client.py
services/
  unpaid_service.py
streamlit_app.py
.env.example
README.md
```

## Setup

1. Clone this repository.
2. Create a `.env` file (see `.env.example`).
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   streamlit run streamlit_app.py
   ```

## Environment Variables

- `COSMOS_ENDPOINT`
- `COSMOS_KEY`
- `COSMOS_DB`
- `COSMOS_CONTAINER_CONTRACTS`
- `COSMOS_CONTAINER_PAYMENTS`
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_API_VERSION`
- `AZURE_OPENAI_DEPLOYMENT_NAME`

## Usage

- Ask questions about tenants and payments in natural language.
- Click "Show unpaid alert" to generate polite reminder messages for unpaid tenants.
- Manage contracts and upload data via the agentic interface.

## License

MIT

