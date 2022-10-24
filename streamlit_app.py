import math
import pandas as pd
import streamlit as st
import random


with st.echo(code_location='below'):
    
    n = random.randrange(1,10)
    guess = st.number_input(label, min_value=1, max_value=10, value= 0, label_visibility="visible")

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
