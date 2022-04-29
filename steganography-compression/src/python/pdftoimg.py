from pdf2image import convert_from_path
import os

outputDir = "imag/"

def convert(file, outputDir):
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    pages = convert_from_path(file, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
    counter =1
    for page in pages:
        myfile=outputDir+'output'+str(counter)+'.jpg'
        counter=counter+1
        page.save(myfile,"JPEG")
        print(myfile)

file="sample.pdf"
convert(file,outputDir)