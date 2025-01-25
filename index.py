import pytesseract as tess
from PIL import Image

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
data = Image.open('image.png')
text = tess.image_to_string(data, lang='khm+eng')

with open("title.txt", "w", encoding="utf-8") as file:
    file.write(text)

print(text)