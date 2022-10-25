import streamlit as st

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}

st.write(list1)
with st.echo(below):
    if st.button("Mean"):
        mean = sum(list1)/len(list1)
        st.write(mean)
    else:
        "Press to calcualate the Mean"

    
    if st.button("Median"):
        if len(list1) % 2 == 0:
            m1 = list1[len(list1)//2]
            m2 = list1[len(list1)//2 - 1]
            median = (m1 + m2)/2
        else:
            median = list1[len(list1)//2]
        st.write(median)
    else:
        "Press to calculate the median"

    if st.button("Mode"):
        for i in list1:
            frequency.setdefault(i, 0)
            frequency[i]+=1

        frequent = max(frequency.values())
        for i, j in frequency.items():
            if j == frequent:
                mode = i
        st.write(mode)
    else:
        "Press to calculate mode"
