import streamlit as st
import base64
import pandas as pd
import imagehash
import binascii
from PIL import Image

def fetchImage(pa):
    file_ = open(pa, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    src = f'src="data:image/gif;base64,{data_url}" style="height: 250px"'
    return src

pa = "Res\Luffy.jpg"
pe = "Res\placeholder.jpg"

# Setting page to utilize Full Body Size
st.set_page_config(layout="wide")
st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>', unsafe_allow_html=True)
st.markdown("# <div style=\"text-align: center;\">Content-based Image Retrieval</div>", unsafe_allow_html=True)
" "
" "
carouselImg = f"""
<div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" {fetchImage(pa)} alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" {fetchImage(pe)} alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" {fetchImage(pa)} alt="Third slide">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
"""

similarImagesContCSS = f"""
<style>
.css-1sdqqxz {{
    background-color: #262730;
    border-radius: 5px !important;
    padding: 20px;

}}
</style>
"""
st.markdown(similarImagesContCSS, unsafe_allow_html=True)
__, col1, __ ,col2, __ = st.columns([1,6,1,5,1])
imgPath = col1.text_input("Image Path:")
col1.markdown("<div style=\"text-align: center;\">─── OR ───</div>", unsafe_allow_html=True)
imgPick = col1.file_uploader("Choose image:")
col2.write("")
similarImgEle = col2.image("Res\placeholder.jpg")
similarImg = None
similarImgHash = None
#S:\College\Resources\2022 - 23 Fall Semester\CSE3501 - Information Security Analysis and Audit\Project\Image Retirval using Perceptual Image Hashing\Res\Luffy.jpg
if imgPath:
    similarImg = Image.open(imgPath)
if imgPick is not None:
    f = open("temp.txt", "wb")
    f.write(imgPick.getvalue())
    f.close()
    similarImg = Image.open("temp.txt")
if similarImg is not None:
    similarImgEle.image(similarImg)
    similarImgHash = imagehash.phash(similarImg)
    col2.markdown(f'<div style="text-align: center;"> Hash Value : {similarImgHash}</div>', unsafe_allow_html=True)
    col2.write(" ")


minThresholdEle = col1.text_input("Minimum threshold required:")
#hashType = col1.selectbox("Hashing Technique :", ["Average hash", "Perceptive hash", "Gradient hash", "Wavelet hashing"])
importType = col1.selectbox("Import Hash Table From :", ["Path", "CSV", "Pickle", "Text File"])
df = None
#pd.DataFrame(hashValues, columns=["Image", "Hash Value"]) 
#dfFrame.dataframe(df)
if importType == "Path":
    importPath = col1.text_input("Enter Path of the Hash Table:")
if importType == "CSV":
    csvBtn = col1.file_uploader("Upload CSV file")
    if csvBtn is not None:
        df = pd.read_csv(csvBtn)
        col2.dataframe(df)
if importType == "Text File":
    txtBtn = col1.file_uploader("Upload Text file")
    if txtBtn is not None:
        df = pd.read_csv(txtBtn, sep=" ")
        col2.dataframe(df)
if importType == "Pickle":
    pklBtn = col1.file_uploader("Upload Pickle file")
    if pklBtn is not None:
        df = pd.read_pickle(pklBtn, compression='infer')
        col2.dataframe(df)

_, _, _, col, _, _, _ = st.columns([1]*6+[1.18])
clicked = col.button('Find Similar images')


# imgCount = len(df["Hash Value"])
listSimilarImages = []
for i in df.index:
    hammingDistance = imagehash.hex_to_hash(df["Hash Value"][i]) - similarImgHash
    if hammingDistance < int(minThresholdEle):
        listSimilarImages.append([df["Path"][i], hammingDistance ])
st.markdown(f"<div style=\"text-align: center;\"> Total number of similar images {len(listSimilarImages)}</div>", unsafe_allow_html=True)
" "
" "
__, cont, __ = st.columns([1,8,1])
for i in listSimilarImages:
    cont.image(Image.open(i[0]))
    cont.markdown(i[0])
    cont.markdown("Hamming Distance = " + str(i[1]))
# for i in range(imgCount):
#     cont.image("Res\placeholder.jpg")

#cont.markdown(carouselImg,unsafe_allow_html=True)
