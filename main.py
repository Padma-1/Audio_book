# TEXT TO SPEECH CONVERTER USING PYTHON
# You must have python and IDE installed on your machine-->here i'm using PyCharm
import pyttsx3  # Python text to speech conversion library
import PyPDF2   # Python PDF library
my_book = open('oop.pdf', 'rb')  # open is a built-in method rb-->reading as a binary book
pdfReader = PyPDF2.PdfFileReader(my_book)
pages = pdfReader.numPages  # to know number of pages in a given book
print(pages)
my_speaker = pyttsx3.init()  # initializing the pyttsx3 library
for i in range(pages):  # to read all pages
    page = pdfReader.getPage(i)
    text = page.extractText()
    my_speaker.say(text)
    my_speaker.runAndWait()
