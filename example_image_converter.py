# code from https://www.geeksforgeeks.org/python-convert-image-to-pdf-using-img2pdf-module/
# Python3 program to convert image to pfd
# using img2pdf library

# importing necessary libraries
import img2pdf
from PIL import Image
import os

# storing image path
img_path = "static/IMG_0296.JPG"

# storing pdf path
pdf_path = "static/new.pdf"

# opening image
image = Image.open(img_path)

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file
file = open(pdf_path, "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# closing image file
image.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file")
