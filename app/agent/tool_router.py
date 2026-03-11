from app.tools.order_tracking_tool import track_order

def tool_router(query):
    if "track order" in query.lower():
        return track_order(query)
    else:
        return "Sorry, I don't have a tool for that query."
    
def agent_response(query):
    return tool_router(query)   

if __name__ == "__main__":
    user_query = input("Please enter your question: ")
    answer = agent_response(user_query)
    print("\nAnswer:\n")
    print(answer)