import streamlit as st

def findlargest(num1,num2,num3):
  findlist=[]
  findlist.append(num1)
  findlist.append(num2)
  findlist.append(num3)
  findlist.sort()
  return findlist[-1]

st.write("""
Welcome to the number finding app on streamlit built by Allan Pais

""")

st.header("User input parameters")

number_1=st.number_input("Enter Number 1", step=1)
number_2=st.number_input("Enter Number 2", step=1)
number_3=st.number_input("Enter Number 3", step=1)

st.write("""
     The Largest number is 
""")


st.write(findlargest(number_1,number_2,number_3))
