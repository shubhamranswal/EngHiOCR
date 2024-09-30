# Manage imports
import pytesseract
from PIL import Image, ImageDraw

# Load OCR model (For Tesseract, there's no specific model to load)
def load_ocr_model():
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\shubh\\Desktop\\Python\\OCR Reader\\Tesseract\\tesseract.exe'
    return None, None

# Perform OCR and get bounding boxes
def perform_ocr(image_file, processor=None, model=None):
    image = Image.open(image_file)
    extracted_text = pytesseract.image_to_string(image, lang='eng+hin')
    boxes = pytesseract.image_to_boxes(image, lang='eng+hin')
    return extracted_text, boxes