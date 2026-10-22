from typing import TypedDict
from langgraph.graph import END, StateGraph

class State(TypedDict):
    number: int

def start(state: State) -> dict:
    boardnum = state["number"]
    
    print("Start")
    print(boardnum)

    return {"number": boardnum}
  
def double(state: State) -> dict:
    boardnum = state["number"]
    newnum = boardnum * 2
    print("-----------")
    print("Double")
    print(newnum)
    return {"number": newnum}


def finish(state: State) -> dict:
    boardnum = state["number"]

    print("-----------")
    print("Finish")
    print(boardnum)

    return {"number": boardnum}

def decision(state: State) -> str:
    if state["number"] < 100:
        return "double"
    else:
        return "finish"

builder = StateGraph(State)

# Add nodes
builder.add_node("start",start)
builder.add_node("double", double)
builder.add_node("finish", finish)

# Set entry point
builder.set_entry_point("start")


# Add conditional edges
builder.add_conditional_edges(
    "start",
    decision,
    {
        "double": "double",
        "finish": "finish"
    }
)

# Add conditional edges
builder.add_conditional_edges(
    "double",
    decision,
    {
        "double": "double",
        "finish": "finish"
    }
)

# Connect finish node to END
builder.add_edge("finish", END)

# Compile graph
graph = builder.compile()

# Execute graph
result = graph.invoke({"number": 105})

print("Final result:", result)
