import streamlit as st

st.title('🎈 Demo')

st.write('Hello world!')
st.write('Hello world!')

x = st.slider("Select a value")
st.write(x, "squared is", x * x)
