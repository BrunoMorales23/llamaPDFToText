import pytesseract
from pdf2image import convert_from_path

def pdfToText():
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    pdf_path = "C:/Users/MarsuDIOS666/Desktop/PDFtoText/30686313677_011_00002_00000129.pdf"
    images = convert_from_path(pdf_path, poppler_path=r"C:/Users/MarsuDIOS666/Desktop/PDFtoText/poppler-24.08.0/Library/bin")

    texto_total = ''
    for i, image in enumerate(images):
        texto = pytesseract.image_to_string(image, lang='eng')
        texto_total += f"\n--- Página {i+1} ---\n{texto}"
    return texto_total