# Python script for snipping text from screen in Windows 

## Install

Install tesseract-ocr  
[https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

Install python (works for 3.9)
[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

Install python modules
```
pip install pytesseract pyperclip
```

Load trained models for wanted languages  
[https://github.com/tesseract-ocr/tessdata_best](https://github.com/tesseract-ocr/tessdata_best)  
and copy it to
```
C:\Program Files\Tesseract-OCR\tessdata\
```

Load  
screen_text_snip.py  
screen_text_snip.bat


Add 'snip.bat' to PATH with
```
set path_to=path\to\screen_text_snip_folder
start /min cmd /c "%path_to%\screen_text_snip.bat" %*
```

## Use

snip **english**

    Press `Win+R`  
    type `snip`  
    open editor  
    Press `Ctrl+C` to insert snipped text  

snip **russian**

	..
    type `snip rus`
    ..
