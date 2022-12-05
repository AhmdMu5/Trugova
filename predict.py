from flask import Flask, render_template, request
import re
import nltk
import pickle   
nltk.download('stopwords')
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('indonesian'))
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.stem.porter import PorterStemmer

factory = StemmerFactory()
stemmer = factory.create_stemmer()

global model,tfidfvect

def load():
    global model,tfidfvect
    model = pickle.load(open('model/model.pkl', 'rb'))
    tfidfvect = pickle.load(open('model/tfidfvect.pkl', 'rb'))

def predict(text):
    teks = re.sub('[^a-zA-Z]', ' ', text)
    teks = teks.lower()
    teks = teks.split()
    teks = [stemmer.stem(word) for word in teks if not word in stopwords.words('indonesian')]
    teks = ' '.join(teks)
    teks_vect = tfidfvect.transform([teks]).toarray()
    if model.predict(teks_vect) == 0:
        prediction = 'Berita Hoax'
    else:
        prediction = 'Sepertinya Benar'
    return prediction