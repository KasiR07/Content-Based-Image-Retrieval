# Abstarct
With the rapid growth of image-based applications and low-cost storage, the size of picture datasets has increased significantly in recent years. Content-based image retrieval (CBIR) is a key feature for these applications, but it can be resource and time-intensive, especially for huge datasets. Perceptual image hashing, a technique that converts images into fixed-size strings and compares them based on their content, has demonstrated promising performance as an alternative to traditional feature extraction methods for CBIR. In this project, we propose a strategy for using perceptual image hashing for CBIR and evaluate its effectiveness through experiments. Our results show that the proposed strategy achieves a high degree of accuracy, making it a promising approach for CBIR applications. We also demonstrate the advantages of using the Multiprocessing package in Python to improve the efficiency of the CBIR process by taking advantage of multiple CPU cores. This allows us to search through large datasets more quickly, making the CBIR system more scalable.

# Introduction
In recent years, there has been a significant increase in the size of picture datasets due to the growth of image-based applications and low-cost storage. As a result, similarity search has become a critical feature for these applications. However, performing these searches can be resource and time-intensive, especially when dealing with large datasets. One approach to addressing this challenge is to extract features from photos and then use these features to perform searches. However, this can still be time-consuming and resource-intensive, particularly with large datasets. Another technique that has shown promising performance is picture hashing, which involves converting an image into a fixed-size string and then using that string to discover related images. Perceptual image hashing, in particular, considers the fingerprint of the images by deriving some features from their contents to calculate similar hash codes for images that have semantically similar content while still generating distinguishable hash codes for images belonging to dissimilar classes. To make the picture hashing process more efficient, parallel processing can be used. The Multiprocessing library in Python allows for the creation of multiple processes that can run concurrently, taking advantage of multiple CPU cores. By splitting the picture hashing process into multiple tasks and assigning them to different processes, the overall processing time can be significantly reduced. This approach is particularly effective when dealing with large datasets, as it enables the processing of multiple images simultaneously, resulting in faster search times and improved performance.

# Libraries Used

1. Multiprocessing - The Multiprocessing library in Python allows for the creation of multiple processes that can run concurrently, taking advantage of multiple CPU cores to improve performance for CPU-bound tasks.[9]
2. Streamlit - Streamlit is an open-source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch,SymPy(latex), NumPy, pandas, Matplotlib etc. [10]
3. Streamlit_nested_layout – Streamlit component that helps with having nested Columns
4. Numpy - NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
5. Pandas - pandas is a software library written for the Python programming language for data manipulation and analysis.
6. OS - Python OS module provides the facility to establish the interaction between the user and the operating system. It offers many useful OS functions that are used to perform OS-based tasks and get related information about operating system.
7. Open CV - OpenCV is a library of programming functions mainly aimed at realtime computer vision.
8. SciPy - SciPy is a free and open-source Python library used for scientific computing and technical computing. SciPy contains modules for optimization, linear algebra, integration, interpolation, special functions, FFT, signal and image processing, ODE solvers and other tasks common in science and engineering.
9. Image Hash - An image hashing library written in Python.
10. Glob - The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order.
11. Pillow - Python Imaging Library is a free and open-source additional library for the Python programming language that adds support for opening, manipulating, and saving many different images file formats.

# Architecture
Image Retrieval 

![image](https://github.com/KasiR07/Content-Based-Image-Retrieval/assets/108777263/8078a484-f844-4217-9c9d-e6d2e037bd81)

Image Retrieval using Perceptual Hashing

![image](https://github.com/KasiR07/Content-Based-Image-Retrieval/assets/108777263/4a439edf-d289-42c4-a8e6-f98ad9d78b8b)

# Proposed Methadology
The suggested hashing algorithm offers experimental proof of the method's performance when compared to methods employing basic characteristics and machine learning methods. The findings demonstrate that the suggested technique performs better and takes significantly less time to produce the hash codes, add them to the tree, and locate related photos. Because of this, it may be utilized in real-time applications. In order to support effective and quick retrieval of related images from image databases, feature extraction is crucial in content-based image retrieval. The definition of the feature is given as a function of one or more measurements, each of which describes a measurable attribute of an item and is calculated in a way that quantifies certain important properties of the object. Color, texture, and shape are considered to be low-level features. We are using Scipy a python framework to convert the pixelmap into a discrete cosine transformation, for different types of DCT, the math model used are:

Type 1:

![image](https://github.com/KasiR07/Content-Based-Image-Retrieval/assets/108777263/cd0bbc84-f765-40d9-adeb-ef8583201190)

Type 2:

![image](https://github.com/KasiR07/Content-Based-Image-Retrieval/assets/108777263/48a38faf-3e63-4839-9943-b74da250eea1)

Type 3:

![image](https://github.com/KasiR07/Content-Based-Image-Retrieval/assets/108777263/352a7e77-1add-467b-9d0c-330bc12c7b83)

Type 4:

![image](https://github.com/KasiR07/Content-Based-Image-Retrieval/assets/108777263/2777ec80-d6e3-4df7-9577-b0a8b82fc56c)

# Results
The use of perceptual image hashing for CBIR offers several advantages. First, it eliminates the need for computationally expensive feature extraction, which makes it a faster and more efficient method. Second, perceptual image hashing can handle large datasets without compromising accuracy. This is particularly useful for applications that involve huge image databases, such as those found on the internet. Third, perceptual image hashing provides a flexible way to compare images based on their content. It can be customized to consider different features, such as color, texture, or shape, depending on the application. Moreover, by using the Multiprocessing package in Python, we were able to further improve the efficiency of the CBIR process. Multiprocessing allowed us to take advantage of the multiple CPU cores available on modern computers, enabling faster execution of CPU-bound tasks. This allowed us to search through large datasets more quickly, making the CBIR system more scalable. Overall, the results and discussions suggest that perceptual image hashing and multiprocessing are promising approaches for CBIR applications. By using these techniques, we can achieve accurate and efficient similarity search without the need for computationally expensive feature extraction. This enables us to search through large image databases more quickly, making CBIR more scalable and applicable to a wide range of applications.

# Conclusion
Moreover, by taking advantage of parallel processing using the Multiprocessing package in Python, we can further improve the efficiency of the CBIR process, enabling us to search through large datasets faster. The Multiprocessing package in Python allows for the creation of multiple processes that can run concurrently, taking advantage of multiple CPU cores to improve performance. This makes it an ideal tool for CBIR applications that involve heavy computation and can be parallelized. By using the Multiprocessing package, we were able to speed up the perceptual image hashing process, reducing the time it takes to obtain photos and making the CBIR system more scalable. While CBIR is a relatively new technique, its potential applications are vast, from image retrieval to medical imaging and beyond. By leveraging the power of perceptual image hashing and parallel processing using the Multiprocessing package in Python, we can unlock the full potential of CBIR and enable new applications that were previously impractical.

# Implementation
Implementing a hash function

![image](https://github.com/KasiR07/Content-Based-Image-Retrieval/assets/108777263/ad127cf9-4446-478c-baec-09c04f2f5b0c)

Converting to grayscale

![image](https://github.com/KasiR07/Content-Based-Image-Retrieval/assets/108777263/a7caac01-319c-4eca-811f-a7c8d0a5e359)

Resizing the image

![image](https://github.com/KasiR07/Content-Based-Image-Retrieval/assets/108777263/211c1722-05c9-479e-94d2-f59d2c9e221d)

Computing the difference and building the hash value

![image](https://github.com/KasiR07/Content-Based-Image-Retrieval/assets/108777263/a21c3cd7-86e7-45ee-be93-6905b2efad52)

Hashing a directory of images

![image](https://github.com/KasiR07/Content-Based-Image-Retrieval/assets/108777263/afb84a9e-4691-4abf-af9f-7fd3dbefe806)

![image](https://github.com/KasiR07/Content-Based-Image-Retrieval/assets/108777263/418321f5-6a0f-4bf5-bc5c-64285d4d2f4d)

Content based Image Retrieval
![image](https://github.com/KasiR07/Content-Based-Image-Retrieval/assets/108777263/90d6b53a-2f7a-4cd8-b318-29b56de0e3aa)

Similar Images

![image](https://github.com/KasiR07/Content-Based-Image-Retrieval/assets/108777263/910b03f0-0804-4b7d-b103-5b4d4e8052d8)

![image](https://github.com/KasiR07/Content-Based-Image-Retrieval/assets/108777263/227a9544-0ad0-4399-9ef9-a419a25fa1f2)
