from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.chains.conversation.memory import ConversationBufferMemory

import streamlit as st


#funcao para calcular numero fibonnaci
def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib (n-2))
    

#definie função para organizar entrada em ordem alfabetica
def sort_string(string):
    return ''.join(sorted(string))


#definir a função para transformar a palavra em criptografada
def encrypt(word):
    encrypted_word = ""
    for letter in word:
        encrypted_word += chr(ord(letter) +1)
    return encrypted_word


#definir a função para descriptografar a palavra
def decrypt(word):
    decrypted_word = ""
    for letter in word:
        decrypted_word += chr(ord(letter) -1)
    return decrypted_word


#chama ferramentas
tools = [
    Tool(
        name = "Fibonnaci",
        func= lambda n: str(fib(int(n))),
        description="usar quando você quiser calcular o nth do numero fibonacci"
        # return_direct=true
    ),
    Tool(
        name = "Sort String",
        func= lambda string: sort_string(string),
        description="usar quando você quiser organizar uma string alfabeticamente"
        # return_direct=true
    ),
    Tool(
        name = "Encrypt",
        func= lambda word: encrypt(word),
        description="usar quando você quiser criptografar uma palavra"

    ),
    Tool(
        name = "Decrypt",
        func= lambda word: decrypt(word),
        description="usar quando você quiser descriptografar uma palavra"
    )
]

memory = ConversationBufferMemory(memory_key="chat_history") 

llm=OpenAI(temperature=0, verbose=True)


#cadeia de atividades
agent_chain = initialize_agent(tools, llm, agent="conversational-react-description",memory=memory, verbose=True)

'''
    if "agent_memory" not in st.session_state:
        st.session_state["agent_memory"] =  ConversationBufferMemory(memory_key="chat_history") # You can use other memory types as well!

llm=OpenAI(temperature=0, verbose=True)
agent_chain = initialize_agent(tools,  llm, agent="conversational-react-description", memory=st.session_state["agent_memory"], verbose=True) # verbose=True to see the agent's thought process'''

''
st.header(":blue[Langchain chatbot com agente, ferramentas e memória] :sunglasses:")
user_input = st.text_input("Você: ")

#inicia buffer de memoria
if "memory" not in st.session_state:
    st.session_state["memory"] = ""

#streamlit botão
if st.button("Envia"):
    st.markdown(agent_chain.run(input=user_input))
    #exibe buffer de memoria
    #adiciona histórico de conversas ao buffer de memoria
    st.session_state["memory"] += memory.buffer
    print(st.session_state["memory"])