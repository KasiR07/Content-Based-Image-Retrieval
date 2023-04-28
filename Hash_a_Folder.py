import streamlit as st
import streamlit_nested_layout
import os
import pandas as pd
import imagehash
import hashes
import time
import glob
from PIL import Image

# @st.cache(suppress_st_warning=True)
# def generateHashValues(path):
#     if path:
#         files = os.listdir(path)
#         images = []
#         flag = False

#         for file in files:
#             if file.endswith((".jpg", ".png", ".jpeg", "JPG", "PNG", "JPEG")):
#                 images.append(file)
        
#         progMsg.text("Hashing the images in the given directory...")
#         progBar = cont.progress(0)
#         cont.write(images)

#         for i, imageName in enumerate(images):
#             image = Image.open(path + "\\" + imageName)
#             hashTemp = imagehash.phash(image)
#             hashValues.append([imageName, str(hashTemp)])
#             progBar.progress((i+1)/len(images))
        
#         if len(images) != 0 and len(hashValues) == len(images):
#             flag = True
#         return flag



# Setting page to utilize Full Body Size
st.set_page_config(layout="wide")
st.markdown("# <div style=\"text-align: center;\">Hashing a Directory of Images</div>", unsafe_allow_html=True)
" "
" "

__, cont, __ = st.columns([1,5,1])

path = cont.text_input("Enter path of directory containing images:")
cont.button("Hash Folder")

progMsg = cont.markdown("")

hashStatus = False
if path:
    x = hashes.hashes(path, cont, progMsg)
    hashStatus, hashValues = x.generateHash()

cont.write(" ")


if hashStatus is not None and hashStatus:
    progMsg.text("Hashing Complete!")
    cont.write(" ")

    dfFrame, __, exportBtns = cont.columns([10,1,6])
    #Panda Data Frame
    df = pd.DataFrame(hashValues, columns=["Image", "Hash Value", "Path"]) 
    dfFrame.dataframe(df)

    # CSV
    csvBtn = exportBtns.button("Export to csv")
    if csvBtn:
        df.to_csv(r"./output/test.csv")

    # Pickle
    pklBtn = exportBtns.button("Pickle the object")
    if pklBtn:
        df.to_pickle(r"./output/pickle")

    # Text File
    txtBtn = exportBtns.button("Export to Text File")
    if txtBtn:
        with open(r"./output/txtTest.txt", "w") as f:
            f.write(df.to_string(header=False, index=False))
