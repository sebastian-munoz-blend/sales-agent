from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
import json

from agents.prompts import SYSTEM_PROMPT
from services.sql_service import execute_query
from services.chart_service import generate_chart
from services.file_service import generate_csv

llm = ChatOllama(model="llama3")

def run_agent(user_input: str):
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_input)
    ]

    response = llm.invoke(messages)

    try:
        result = json.loads(response.content)
    except:
        print("Error interpretando respuesta:")
        print(response.content)
        return None

    sql = result["sql"]
    action = result["action"]

    print("\nSQL generado:\n", sql)

    df = execute_query(sql)

    # Decidir acción
    if action == "chart":
        file = generate_chart(df)
        return f"Gráfico generado: {file}", df

    elif action == "csv":
        file = generate_csv(df)
        return f"Archivo generado: {file}", df

    else:
        return df, None