import PIL.Image
import easyocr
import numpy as np

class OCREngine:
    def __init__(self):
        # This will download the model once (about 100MB)
        self.reader = easyocr.Reader(['en'])

    def extract_text(self, image):
        try:
            # EasyOCR needs a numpy array or a path
            image_np = np.array(image)
            results = self.reader.readtext(image_np, detail=0)
            
            # Join all detected text into one string
            full_text = " ".join(results)
            return full_text
        except Exception as e:
            print(f"OCR Error: {e}")
            return ""