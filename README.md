# ScreenShot2PDF
Take screenshots and put them to a pdf file
## Why should I use this?
This makes screenshotting en masse much easier. If you want to save your teacher's slides/ presentation for later you can simply use this
to get everything you need in a compact [(maybe even searchable 👀)] (https://ocr.space) PDF format.  
## How to use this?
Configure `main.py` (namely the global variables `IMAGE_PATH`, `PEDOFILE_PATH`, `KEYS`) and run.  
While `main.py` is running you can take a screenshot by pressing every key in `KEYS` (`i` and `o` by default).  
The screenshots will be saved in `IMAGE_PATH` as `IMAGE_PATH\{index}.png` while the PDF file will be saved as `PEDOFILE_PATH` (make sure this path ends in `.pdf`).  
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
Either minimize the window or rename `main.py` to `main.pyw`  
but this will make it harder to close
