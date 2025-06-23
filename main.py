import streamlit as st
st.title("Interactive Streamlit App !!! ")
st.write("Hello !! Creating a simple web application using streamlit . ")
#Taking user input
name=st.text_input("Enter Your name : ")
#Displaying a message when a button is clicked
if st.button("Submit"):
  st.write(f"Hello, {name} !! Welcome to streamlit. ")


