import streamlit as st


def calculator():
    st.title("Calculator App")
     # Adding images
    st.image("calc.png", width=200)
   


    menu = ["Addition", "Subtraction", "Multiplication", "Division", "Modulus", "Exponentiation", "Floor Division"]
    choice = st.sidebar.selectbox("Select an operation", menu)
    num1 = st.number_input("Enter the first number", step=1.0)
    num2 = st.number_input("Enter the second number", step=1.0)

    if st.button("Calculate"):
        if choice == "Addition":
            result = num1 + num2
            st.success(f"The sum of {num1} and {num2} is {result}")
        elif choice == "Subtraction":
            result = num1 - num2
            st.success(f"The difference between {num1} and {num2} is {result}")
        elif choice == "Multiplication":
            result = num1 * num2
            st.success(f"The product of {num1} and {num2} is {result}")
        elif choice == "Division":
            if num2 == 0:
                st.error("Error: Division by zero!")
            else:
                result = num1 / num2
                st.success(f"The quotient of {num1} and {num2} is {result}")
        elif choice == "Modulus":
            result = num1 % num2
            st.success(f"The modulus of {num1} and {num2} is {result}")
        elif choice == "Exponentiation":
            result = num1 ** num2
            st.success(f"{num1} to the power of {num2} is {result}")
        elif choice == "Floor Division":
            if num2 == 0:
                st.error("Error: Division by zero!")
            else:
                result = num1 // num2
                st.success(f"The floor division of {num1} and {num2} is {result}")
        else:
            st.error("Invalid input. Please try again.")

if __name__ == "__main__":
    calculator()
