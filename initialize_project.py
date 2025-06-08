# 📁 rent-agent-hackathon/ プロジェクト構成を自動でセットアップするスクリプト

import os

folders = [
    "services",
    "agents",
    "data",
    "utils",
    "notebooks"
]

files = {
    "services/__init__.py": "",
    "services/cosmos_client.py": "# 既存ファイルをここに移動してください\n",
    "agents/__init__.py": "",
    "agents/upload_agent.py": "# CSVからCosmosDBにアップロードする処理を書く\n",
    "agents/query_agent.py": "# CosmosDBから問い合わせを行う処理を書く\n",
    "utils/__init__.py": "",
    "README.md": "# Rent Agent Hackathon Project\n\n説明をここに書きます。\n",
    "test_connection.py": "# 既存ファイルをここに移動してください\n"
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("✅ プロジェクト構成を初期化しました！")