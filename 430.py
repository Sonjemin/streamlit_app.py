# streamlit_app.py
import streamlit as st
from openai import OpenAI

api_key= st.text_input("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", type="password")
client = OpenAI(api_key=api_key)

st.title("OpenAI GPT model")

prompt = st.text_area("User prompt")

if st.button("Ask!", disabled=(len(prompt)==0)):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    st.write(response.output_text)
