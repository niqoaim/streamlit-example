import math
import pandas as pd
import streamlit as st
import random

n = random.randrange(1,10)

with st.echo(code_location='below'):
    guess = st.slider("Guess a Number", 1, 5000, 2000)

    while n!= guess:
        if guess < n:
           print("Too low")
           guess = int(input("Enter number again: "))
        elif guess > n:
            print("Too high!")
            guess = int(input("Enter number again: "))
        else:
        break
print("you guessed it right!!")
