import math
import pandas as pd
import streamlit as st
import random


with st.echo(code_location='below'):
    guess = st.slider("Guess a Number", 0, 10, 0)
    n = random.randrange(1,10)

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
