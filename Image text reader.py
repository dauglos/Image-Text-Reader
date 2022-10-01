import pytesseract
import cv2

#Reading the image
image = cv2.imread('textsample.png')

#Using tesseract to extract text from the image
path = r'C:\Program Files\Tesseract-OCR'
pytesseract.pytesseract.tesseract_cmd = path + r'\tesseract.exe'
text = pytesseract.image_to_string(image)
print(text)
