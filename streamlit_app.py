import streamlit as st

list1 = [20, 30, 40, 50, 60, 20, 70 ,10, 90, 20]
frequency = {}

"List of numbers"
st.write(list1)
with st.echo(code_location="below"):
    if st.button("Mean"):
        mean = sum(list1)/len(list1)
        st.write(mean)
    else:
        "Press to calculate the Mean"

    
    if st.button("Median"):
        if len(list1) % 2 == 0:
            m1 = list1[len(list1)//2]
            m2 = list1[len(list1)//2 - 1]
            median = (m1 + m2)/2
        else:
            median = list1[len(list1)//2]
        st.write(median)
    else:
        "Press to calculate the Median"

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
        "Press to calculate Mode"
    "And here's how its done!"
