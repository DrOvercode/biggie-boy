import streamlit as st
import requests
import json


url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

st.title("Aerospace Engineer Chatbot")

user_input = st.text_input("Your question to Mr. Armstrong: ")

if st.button("Send"):
    data = {"model": "ALIENTELLIGENCE/aerospaceengineer", "prompt": user_input, "stream": False}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        st.write("Mr. Armstrong: ", actual_response)
    else:
        st.write("Error:", response.status_code, response.text)

@app.post("/chat")
async def chat(message: str, request: Request):
    # Send the message to the Streamlit chatbot
    response = chatbot.send_message(message)
    return {"response": response}

@app.get("/response")
async def response():
    # Retrieve the chatbot's response from Streamlit
    response = chatbot.get_response()
    return {"response": response}
