from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# print(pytesseract.image_to_string(Image.open('bg.jpg')))
inp = input("Enter your input filename: ")
x = pytesseract.image_to_string(Image.open(inp))
# print(type(x))
name = input("enter the output filename: ") #enter .txt after entering the filename
filename = name+".txt"
with open(filename, "w") as f:
    f.write(x)
    f.close()
