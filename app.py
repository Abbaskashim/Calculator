import streamlit as st

def calculate(num1, num2, operation):
    if operation == "➕":
        return num1 + num2
    elif operation == "➖":
        return num1 - num2
    elif operation == "✖":
        return num1 * num2
    elif operation == "➗":
        if num2 == 0:
            return None
        return num1 / num2

st.title("📱 Simple Calculator App")
st.subheader("A user-friendly calculator built with Streamlit")

num1 = st.number_input("Enter the first number:", step=1)
num2 = st.number_input("Enter the second number:", step=1)

operation = st.selectbox("Select an operation:", ["➕", "➖", "✖", "➗"])

if operation == "➗" and num2 == 0:
    st.warning("Divided by zero is not allowed!")
else:
    if st.button("Calculate"):
        result = calculate(num1, num2, operation)
        st.subheader(f"Result: {result}")
