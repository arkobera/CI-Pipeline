import streamlit as st

st.title("Square and Cube Calculator")

number = st.number_input("Enter a number:", value=0.0)

if st.button("Calculate"):
    square = number ** 2
    cube = number ** 3
    st.write(f"Square of {number} is {square}")
    st.write(f"Cube of {number} is {cube}")
