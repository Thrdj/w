#pip install langdetect

#importing library
from csv import reader
from langdetect import detect

#talking input from user
text = input("Enter any text in any language: ")

#printng output
print(detect(text))

#QR Code using Python
#stuck pyqrcode not working#
import pyqrcode
import png
link = "https://www.w3schools.com/python/"
qr_code = pyqrcode.create(link)
qr_code.png("qrcode_www.w3schools.com.png", scale=5)

#Decode a QR Code using Python
from pyzbar.pyzbar import decode
from PLT import Image
decocdeQR = decode(Image.open('qrcode_www.w3schools.com.png'))
print(decocdeQR[0].data.decode('ascii'))

#Spelling Correction
from textblob import TextBlob
def Convert(string):
    li = list(string.split())
    return li
strl = input("Enter your word : ")
words=Convert(strl)
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words :", words)
print("Corrected Words are :")
for i in corrected_words:
    print(i.correct(),end="")

#Extract Text from PDF
import PyPDF2
pdf = open("pythonclcoding.pdf","rb")
reader = PyPDF2.PdffileReader(pdf)
page = reader.getPage(0)
print(page.extractText())

#Unzip Files using Python
from zipfile import ZipFile
with ZipFile('binod.zip','r') as zip_object:
    zip_object.extractall()
#list of files that are archived in the ZIP file
print(zip_object.namelist())

#clcoding.com