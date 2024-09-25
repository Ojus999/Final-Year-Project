import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(u'SSN College of Engineering is the best college')
displacy.serve(doc, style='ent')