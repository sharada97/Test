import streamlit as st

st.title("👋 Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")

# Text input
name = st.text_input("What's your name?", "World")
st.write(f"Hello, {name}!")

# Number input
number = st.slider("Pick a number", 0, 100, 50)
st.write(f"You picked: {number}")

# Button
if st.button("Say Hello"):
    st.success(f"👋 Hello, {name}! You picked {number}.")

