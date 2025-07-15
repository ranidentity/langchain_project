from model.state import State, graph_builder, START, END
from common.init_groq import init_groq

model = init_groq()

## chatbot langgraph
def chatbot(state: State):
    return {"messages":[model.invoke(state["messages"])]}

graph_builder.add_node("chatbot",chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()

def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)