import os
from agents.query_agent import handle_user_query

def main():
    while True:
        query = input("質問を入力してください（終了するには 'exit' と入力）：\n> ")
        if query.lower() in ["exit", "終了"]:
            break
        answer = handle_user_query(query)
        print("🔎 回答:", answer)

if __name__ == "__main__":
    main()