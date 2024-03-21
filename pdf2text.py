# import module  
import PyPDF2 

# path of PDF 
path = open('file.pdf', 'rb') 

# creat a PdfReader object 
pdfReader = PyPDF2.PdfReader(path) 

# start at the 5th page  
# read the page. 
from_page = pdfReader.pages[4] 

# extracting the text from the PDF 
text = from_page.extract_text() 

print(text)
