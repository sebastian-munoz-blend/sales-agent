from db.database import init_db
from agents.agent import run_agent

init_db()

while True:
    user_input = input("\nPregunta: ")

    result = run_agent(user_input)

    if result:
        df, action = result

        print("\nResultado:")
        print(df)