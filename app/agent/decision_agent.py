from langchain_openai import ChatOpenAI
from app.rag.retrieval_engine import retrieve_relevant_documents
from app.tools.order_tracking_tool import order_status_tool
from app.tools.product_info_tool import get_product_info
from app.agent.memory_manager import add_to_memory, get_memory


class DecisionAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0.7)

    def tool_router(self, query):
        if "track order" in query.lower():
            return order_status_tool(query)
        elif "product" in query.lower():
            product_id = query.split()[-1]
            return get_product_info(product_id)
        else:
            return None

    def generate_response(self, query):

        # Step 1: Try tools first
        tool_response = self.tool_router(query)

        if tool_response:
            add_to_memory(query, tool_response)
            return tool_response

        # Step 2: Retrieve docs
        relevant_docs = retrieve_relevant_documents(query)

        context = "\n\n".join([doc.page_content for doc in relevant_docs])

        chat_history = get_memory()

        prompt = f"""
You are a helpful customer support assistant.

Chat History:
{chat_history}

FAQ Context:
{context}

User Question:
{query}

Provide a helpful answer.
"""

        response = self.llm.invoke(prompt)

        add_to_memory(query, response.content)

        return response.content


if __name__ == "__main__":
    agent = DecisionAgent()
    user_query = input("Please enter your question: ")
    answer = agent.generate_response(user_query)

    print("\nAnswer:\n")
    print(answer)