import streamlit as st

st.title("A quick app")

prompt = st.chat_input("Enter your equation")
if prompt:
    # process the equation
    st.write(f"The equation entere is {prompt}")