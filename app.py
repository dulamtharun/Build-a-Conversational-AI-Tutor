import streamlit as st
import google.generativeai as genai

st.snow()

st.title("💬AI Chatbot🧾")

f = open(r"C:\\Users\\lenovo\\Desktop\\DS\\internship\\task-4\\AI Chatbot.txt")
key = f.read()

genai.configure(api_key=key)

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              system_instruction="""you are a helpful AI teaching assistance.
                              You need to answer the question of the user provided in a polite manner, if you don't know the 
                              answer then you should ask the user I am not able to provide the right now.""")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"]=[]

chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt = st.chat_input()

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response = chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state["chat_history"]=chat.history
