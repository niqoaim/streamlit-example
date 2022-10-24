import math
import pandas as pd
import streamlit as st
import random

n = random.randrange(1,10)
guess = st.slider("Guess a Number", 1, 10, 5)

while n!= guess:
    if guess < n:
        st.write("Too low")
    elif guess > n:
        st.write("Too high!")
    else:
        break
        
st.write(
