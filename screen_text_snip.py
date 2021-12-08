import os
import sys

from PIL import Image, ImageGrab

from pytesseract import pytesseract
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

import pyperclip


def makeImageClip():
    os.system('SnippingTool.exe /clip')

def grabImageFromClipboard():
    return ImageGrab.grabclipboard().convert()

def extractTextFromImage(img:Image) -> str:
    lang = f'{sys.argv[1] if len(sys.argv) > 1 else "eng"}'
    print(f"{lang=}")
    return pytesseract.image_to_string(img, lang=lang)

def main():
    makeImageClip()
    try:
        img = grabImageFromClipboard()
        text = extractTextFromImage(img)
        print(text)
        pyperclip.copy(text)    
    except Exception as e:
        pyperclip.copy(str(e)) 
     
if __name__ == "__main__":
    print(pytesseract.get_languages())
    main()
    #print(sys.argv)   