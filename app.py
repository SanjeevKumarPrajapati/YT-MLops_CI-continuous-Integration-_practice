import streamlit as st

#streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square,cube,and fifth power.")

#get the user input

n=st.number_input("Enter an integer",value=1,step=1)

#Calculate the result
square=n**2
cube=n**3
fifth_power=n**5

#display the results
st.write(f"The square of {n} is : {square}")
st.write(f"The Cube of {n} is : {cube}")
st.write(f"The fifth power of {n} : {fifth_power}")
