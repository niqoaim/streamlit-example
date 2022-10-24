import math
import pandas as pd
import streamlit as st
import random

n = random.randrange(1,10)

with st.echo(code_location='below'):
    guess = st.slider("Guess a Number", 0, 10, 0)

    while n!= guess:
        if guess < n:
            st.write("Too low")
            n == n
            break
        elif guess > n:
            st.write("Too high!")
            n == n
            break
        else:
            break
    st.write(n)
