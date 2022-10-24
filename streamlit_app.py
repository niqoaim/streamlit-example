import math
import streamlit as st
import random

if st.button('Randomise'):
    n = random.randrange(1,10)
else:
    
with st.echo(code_location='below'):

     n = random.randrange(1,10)
     guess = st.number_input("Take a guess", min_value=0, max_value=10, value=0, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

     while n!= guess:
         if guess < n:
            st.write("Too low")
            break
         elif guess > n:
            st.write("Too high!")
            break
         else:
            break
st.write(n)
