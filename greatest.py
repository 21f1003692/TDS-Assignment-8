import streamlit as st

st.title('Greatest among 3 numbers')
a = st.number_input('Enter first number')
b = st.number_input('Enter second number')
c = st.number_input('Enter third number')
if (a >= b) and (a >= c):
   result = a
elif (b >= a) and (b >= c):
   result = b
else:
   result = c
st.write('Greatest Number: ', result)
