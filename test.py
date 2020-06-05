from __future__ import unicode_literals

import pandas as pd
from bs4 import BeautifulSoup as bs

from hazm import *
from hazm import stopwords_list

stemmer = Stemmer()
print(stemmer.stem('کارشناس'))

lemmatizer = Lemmatizer()
print(lemmatizer.lemmatize('کارشناس'))

# tagger = POSTagger(model='resources/postagger.model')
# print(tagger.tag(word_tokenize('کتاب‌ها')))

# lemmatizer = Lemmatizer()
# print(lemmatizer.lemmatize('کتاب‌ها'))

# print(lemmatizer.lemmatize('می‌روم').split('#')[1])