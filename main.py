import pyttsx3
import PyPDF2
import tkinter.filedialog as tk

document = tk.askopenfilename(filetypes=[('pdf', '*.pdf')], defaultextension = [('pdf', '*.pdf')])
pdfreader = PyPDF2.PdfFileReader(document)
pagesNum = pdfreader.numPages
wholeDoc = "" # initialise the string to save to mp3

# Filters the page number which is located at the bottom of every page
# and then saves the output as an mp3
for i in range(0, pagesNum):
    page = pdfreader.getPage(i)
    print(i) # prints current page number
    text = page.extractText()
    engine = pyttsx3.init()
    # if the last line contains a number, remove it so it is not read 
    if text.splitlines()[-1].isdigit():
        text = "\n".join(text.splitlines()[0:-1])
    wholeDoc += text

    # opens save dialog when last page is reached
    if i == pagesNum - 1:
        file = tk.asksaveasfile(mode='w', filetypes=[('mp3', '*.mp3')], defaultextension = [('mp3', '*.mp3')])
        file.close()
        engine.save_to_file(wholeDoc, file.name)
    engine.runAndWait()
