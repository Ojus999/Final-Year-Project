from PyPDF2 import PdfReader
import spacy
from spacy import displacy

reader = PdfReader("Resume 3.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(text)