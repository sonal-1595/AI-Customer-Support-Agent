from langchain_classic.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key="chat_history"
                                    , return_messages=True)

def add_to_memory(user_input, agent_response):
    memory.save_context({"input": user_input}, {"output": agent_response})  

def get_memory():
    return memory.load_memory_variables({})["chat_history"]

