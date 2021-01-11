# ScreenShot2PDF
Take screenshots and put them in a pdf file
## Why should I use this?
This makes screenshotting en masse much easier. If you want to save your teacher's slides/ presentation for later you can simply use this 
to get everything you need in a compact (maybe even searchable) PDF format.  
## How to use this?
Install `python` and all packages from `requirements.txt` (`pip install -r requirements.txt` in the directory with `requirements.txt`).
Configure `main.py` (namely the global variables `TRY_TO_OCR`, `IMAGE_PATH`, `PEDOFILE_PATH`, `KEYS`) and run.
While `main.py` is running you can take a screenshot by pressing every key in `KEYS` (`i` and `o` by default).
The screenshots will be saved in `IMAGE_PATH` as `IMAGE_PATH\{index}.png` while the PDF file will be saved as `PEDOFILE_PATH` (make sure this path ends in `.pdf`).
## OCR
If you want to use ocr install [this](https://github.com/jbarlow83/OCRmyPDF) first and then set `TRY_TO_OCR` to `True`.
### I want to crop a part of my screenshots out
Run `main` from `to_pdf.py` with
* `output_path` as the location you want your pdf to be
* `glob_path` as the location of your screenshot folder (same as your `IMAGE_PATH` in `main.py`)
* `func` as `lambda x: x.crop((?, ?, ?, ?))` with actual numbers instead of `?` (this is in the `to_pdf.py` file as an example)
### I accidentally screenshotted something I don't want to put in a PDF
Simply delete the image from the `IMAGE_PATH` directory and run `to_pdf.py` with
* `output_path` as the location you want your pdf to be
* `glob_path` as the location of your screenshot folder (same as your `IMAGE_PATH` in `main.py`)
### The window is annoying and I don't want to see it
Either minimize the window or rename `main.py` to `main.pyw` but this will make it harder to close.
