import streamlit as st

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

st.write(list1)
if st.button("Mean"):
    mean = sum(list1)/len(list1)
    st.write(mean)
else:
    "Press to calcualate the Mean"
    
