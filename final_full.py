# importing the modules  
import PyPDF2 
from gtts import gTTS

# path of the PDF file 
path = open('file.pdf', 'rb') 

# creating a PdfReader object 
pdfReader = PyPDF2.PdfReader(path) 

# the page with which you want to start 
# this will read the page. 
from_page = pdfReader.pages[4] 

# extracting the text from the PDF 
text = from_page.extract_text() 

language = 'en'

# reading the text 
speak = gTTS(text=text, lang=language, slow=False)
speak.save("test.mp3")
