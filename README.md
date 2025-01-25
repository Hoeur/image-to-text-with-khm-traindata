# Khmer OCR using Tesseract and Python

This project extracts text from images using Tesseract OCR with the Khmer language, utilizing an updated Khmer trained data model.

## Prerequisites

Make sure you have the following installed:

- Python (>=3.7)
- Tesseract-OCR with updated Khmer trained data
- Required Python libraries (`pytesseract`, `PIL`)

## Installation

### 1. Install Python and Required Libraries

```sh
pip install pytesseract pillow
```

### 2. Install Tesseract-OCR

Download and install Tesseract OCR from:

- [Tesseract OCR Download](https://github.com/UB-Mannheim/tesseract/wiki)

Ensure you have the latest Khmer trained data (`khm.traineddata`). You can download it from:

- [Tesseract Trained Data](https://github.com/tesseract-ocr/tessdata)

Place the `khm.traineddata` file into the `tessdata` directory inside your Tesseract installation folder.

To verify installed languages, run:

```sh
tesseract --list-langs
```

### 3. Set Up Tesseract Path

Find where Tesseract is installed (default on Windows):

```sh
C:\Program Files\Tesseract-OCR\tesseract.exe
```

Update your Python script to point to this location:

```python
import pytesseract as tess
from PIL import Image

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## Usage

1. Place your image (`image.png`) in the project directory.
2. Run the script:

```sh
python script.py
```

3. Extracted text will be saved to `title.txt` and displayed in the console.

## Troubleshooting

- Ensure `tesseract.exe` path is correct.
- Confirm the latest `khm.traineddata` is installed in the `tessdata` folder.
- Run `tesseract --list-langs` to verify Khmer support.
- If text output is incorrect, try using a clearer image or apply preprocessing techniques.

## License

This project is open-source and free to use.

