import requests
import streamlit as st

# Function to call FastAPI backend
def get_groq_response(user_input):
    json_body = {
        "input": {
            "language": "French",  # You can later make this dynamic
            "text": user_input
        },
        "config": {},
        "kwargs": {}
    }

    try:
        response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Streamlit frontend
st.title("LLM Application Using LCEL")

input_text = st.text_input("Enter the text you want to convert to French:")

if input_text:
    result = get_groq_response(input_text)

    # Display translated output
    st.write("Translated Output:")
    if "output" in result:
        st.success(result["output"])
    else:
        st.error(result.get("error", "Unexpected error occurred"))