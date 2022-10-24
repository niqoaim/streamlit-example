import math
import streamlit as st
import random
n = 0
if st.button('Randomise'):
    n = random.randrange(1,10)
else:
    "click the button to start"
    
with st.echo(code_location='below'):
     guess = st.number_input("Guess 1", min_value=0, max_value=10, value=0, step=1, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
     while n!= guess:
          if guess < n:
             st.write("Too low")
             break
             guess = st.number_input("Guess 2", min_value=0, max_value=10, value=0, step=1, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
          elif guess > n:
             st.write("Too high!")
             break
             guess = st.number_input("Guess 3", min_value=0, max_value=10, value=0, step=1, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
          else:
             st.write("Congrats you guessed it!")

st.write(n)
