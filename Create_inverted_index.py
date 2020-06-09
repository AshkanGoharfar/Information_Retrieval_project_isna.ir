from __future__ import unicode_literals

import pandas as pd
from bs4 import BeautifulSoup as bs

from hazm import *
from hazm import stopwords_list

import string

import time

english_alphabet = list(string.ascii_lowercase)
for item in list(string.ascii_uppercase):
    english_alphabet.append(item)
# print(english_alphabet)

stop_words = ['»', '.', '«', '،', '؟', '"', '#', ')', '(', '*', ',', '-', '/', ':', '[', ']', '،', '?', '…', '۰', '۱',
              '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '-', '+', '=', '@', '$', '$', '%', '^', '&', '-', '_', '{', '}',
              '\'', '/', ';', '  ', '>', '<', '•', '٪', '؛']
persian_alphabet = ["ا", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د", "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض", "ط", "ظ",
                    "ع", "غ", "ف", "ق",
                    "ک", "گ", "ل", "م", "ن", "و", "ه", "ی"]

for item in english_alphabet:
    stop_words.append(item)

for item in persian_alphabet:
    stop_words.append(' ' + item + ' ')

print(stop_words)


def extract_token():
    start_time = time.time()
    df = pd.read_csv('ir-news-0-2.csv', delimiter=',')
    dictionary = []
    lemmatizer = Lemmatizer()
    for i in range(len(df['content'])):
        soup = bs(df['content'][i])
        text = soup.get_text()
        # print(text)
        dic = {}
        # parsing the text
        lines = text.splitlines()
        parag = []
        terms = []
        parag.append([i])

        for line in lines:
            # check if line has ':', if it doesn't, move to the next line
            if line.find(':') == -1:
                continue

            # Normalize each line
            normalizer = Normalizer()
            line = normalizer.normalize(line)
            flag = 0
            for j in range(len(stop_words)):
                if stop_words[j] in line:
                    line = line.replace(stop_words[j], ' ')
                if '  ' in line:
                    line = line.replace('  ', ' ')
            for element in line.split(' '):
                l = 0
                while flag == 0 and l < len(dictionary):
                    if '#' in lemmatizer.lemmatize(element) and lemmatizer.lemmatize(element).split('#')[1] == \
                            dictionary[l][0] and i not in dictionary[l][2]:
                        # print('# ! : ' + str(lemmatizer.lemmatize(element)))
                        dictionary[l][1] += 1
                        dictionary[l][2].append(i)
                        flag = 1
                    elif element == dictionary[l][0] and i not in dictionary[l][2]:
                        dictionary[l][1] += 1
                        dictionary[l][2].append(i)
                        flag = 1
                    l += 1

                if flag == 0:
                    if '#' in lemmatizer.lemmatize(element):
                        dictionary.append([lemmatizer.lemmatize(element).split('#')[1], 1, [i]])
                    elif element != '':
                        dictionary.append([element, 1, [i]])
        # print(dictionary)
    print("--- %s seconds ---" % (time.time() - start_time))
    return dictionary


print(extract_token())
