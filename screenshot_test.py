#-- include('examples/showgrabbox.py')--#
import pyscreenshot as ImageGrab
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import time
import os.path

if __name__ == "__main__":
    # part of the screen
    im=ImageGrab.grab(bbox=(528,260,616,304)) # X1,Y1,X2,Y2
    text = pytesseract.image_to_string(im)
    print(text)
#-#