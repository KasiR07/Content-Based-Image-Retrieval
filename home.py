import streamlit as st
import os

# Setting page to utilize Full Body Size
st.set_page_config(layout="wide")


st.markdown("# <div style=\"text-align: center;\">Content-based Image Retrieval</div>", unsafe_allow_html=True)
" "
" "
__, col1, __ ,col2, __ = st.columns([1,6,1,5,1])
col1.container()

imgPath = col1.text_input("Image Path:")

col1.markdown("<div style=\"text-align: center;\">─── OR ───</div>", unsafe_allow_html=True)
imgPick = col1.file_uploader("Choose image:")
minThreshold = col1.text_input("Minimum threshold required:")
hashType = col1.selectbox("Hashing Technique :", ["Average hash", "Perceptive hash", "Gradient hash", "Wavelet hashing"])

col2.write("")
col2.image("Res\placeholder.jpg")