import streamlit as st
# package name: pillow (pip3 install pillow)
from PIL import Image

image = Image.open(uploaded_file).convert('RGB')
st.title('Hello Dillon')
st.header('CNN Project')
st.write('This is my first Streamlit app')


