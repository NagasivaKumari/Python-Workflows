
import streamlit as st

st.title("DevOps Workflow for Python Applications")
st.write("This is a sample Streamlit app deployed with a DevOps workflow.")

def add(a, b):
    return a + b

num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

if st.button("Add"):
    result = add(num1, num2)
    st.success(f"Result: {num1} + {num2} = {result}")

