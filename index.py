import pytesseract as tess
from PIL import Image, ImageEnhance, ImageFilter

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image
image = Image.open('image.png')

# Convert the image to grayscale
image = image.convert('L')

# Enhance the image contrast
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(2)

# Apply a filter to sharpen the image
image = image.filter(ImageFilter.SHAPEN)

# Save the preprocessed image (optional, for debugging purposes)
image.save('preprocessed_image.png')

# Perform OCR on the preprocessed image
text = tess.image_to_string(image, lang='khm+eng')

# Write the extracted text to a file
with open("title.txt", "w", encoding="utf-8") as file:
    file.write(text)

print(text)