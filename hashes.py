import scipy.fftpack
import streamlit as st
import os
import glob
from PIL import Image
import imagehash

class hashes:
    def __init__(self, path, cont, progMsg):
        self.path = path
        self.flag = False
        self.Files = glob.glob(path + '/**/*.*', recursive=True)
        self.images = []
        self.hashValues = []
        self.cont = cont
        self.progMsg = progMsg

        for file in self.Files:
                if file.endswith((".jpg")):
                    self.images.append(file)

    @st.cache(hash_funcs = {st.delta_generator.DeltaGenerator: lambda _: None}, suppress_st_warning=True)
    def generateHash(self):

        self.progMsg.text(f"Hashing the images in the given directory...")
        progBar = self.cont.progress(0)
        for i, imagePath in enumerate(self.images):
            image = Image.open(imagePath)
            imageName = os.path.basename(imagePath)
            hashTemp = imagehash.phash(image)
            self.hashValues.append([imageName, str(hashTemp), imagePath])
            self.progMsg.text(f"Hashing the images in the given directory... ({i+1}/{len(self.images)})")
            progBar.progress((i+1)/len(self.images))
        
        if len(self.images) != 0 and len(self.hashValues) == len(self.images):
            self.flag = True

        return (self.flag, self.hashValues)