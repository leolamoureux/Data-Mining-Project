# pip install spacy
# pip install spacy_langdetect
# python3.10 -m spacy download en_core_web_sm

import langdetect

def detect_language(text):
    return langdetect.detect(text)

# Example usage
text = "This is an example of a large text. It is written in English, but it could contain text in other languages as well."
print(detect_language(text))

'''import pandas as pd
import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector

def get_lang_detector(nlp, name):
    return LanguageDetector()

nlp = spacy.load("en_core_web_sm")
Language.factory("language_detector", func=get_lang_detector)
nlp.add_pipe('language_detector', last=True)

df = pd.read_csv('articles.csv')
#df = df[['text']]

i = 1 # Numéro tuple
for text in df['text']:
    doc = nlp(text)
    if doc._.language['language'] != 'en':
        print(str(i) + str(doc._.language))
    i += 1'''