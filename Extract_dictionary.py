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

stop_words = ['»', '.', '«', '،', '؟', '"', '#', ')', '(', '*', ',', '-', '/', ':', '[', ']', '،', '?', '…', '۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '-', '+', '=', '@', '$', '$', '%', '^', '&', '-', '_', '{', '}', '\'', '/', ';', '  ', '>', '<', '•', '٪', '؛']
persian_alphabet = ["ا", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د", "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق",
  "ک", "گ", "ل", "م", "ن", "و", "ه", "ی"]

for item in english_alphabet:
    stop_words.append(item)

for item in persian_alphabet:
    stop_words.append(' ' + item + ' ')

print(stop_words)

def extract_token():
    start_time = time.time()
    df = pd.read_csv('ir-news-0-2.csv', delimiter=',')
    dict_term = []

    dictionary = []
    lemmatizer = Lemmatizer()
    stemmer = Stemmer()

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
            # print(line)
            # print('##########')
            flag = 0
            for j in range(len(stop_words)):
                if stop_words[j] in line:
                    line = line.replace(stop_words[j], ' ')
                if '  ' in line:
                    line = line.replace('  ', ' ')
            # print(line)
            # print('*********************')

            for element in line.split(' '):
                for l in range(len(dictionary)):
                    if '#' in lemmatizer.lemmatize(element):
                        # print('# ! : ' + str(lemmatizer.lemmatize(element)))
                        if lemmatizer.lemmatize(element).split('#')[1] == dictionary[l][0] and i not in dictionary[l][2]:
                            dictionary[l][1] += 1
                            dictionary[l][2].append(i)
                            flag = 1
                            # print('repeated noun term !' + str(stemmer.stem(element)) + str(dictionary[l][1]) + str(dictionary[l][2]))
                    # elif stemmer.stem(element) == dictionary[l][0] and 'i' not in dictionary[l][2]:
                    elif i not in dictionary[l][2]:
                        dictionary[l][1] += 1
                        dictionary[l][2].append(i)
                        # print('repeated verb term !' + str(stemmer.stem(element)) + str(dictionary[l][1]) + str(dictionary[l][2]))
                        flag = 1

                if flag == 0:
                    if '#' in lemmatizer.lemmatize(element):
                        # print('new verb term 1 !' + str(element))
                        # print('new verb term 2 !' + str(lemmatizer.lemmatize(element).split('#')[1]) + '1' + str(i))
                        dictionary.append([lemmatizer.lemmatize(element).split('#')[1], 1, [i]])
                    elif element != '':
                    #     # print('new noun term 1 !' + str(element))
                        dictionary.append([element, 1, [i]])
                    #     # print('new noun term 2 !' + str(
                    #     #     lemmatizer.lemmatize(element)) + '1' + str(i))
        print(dictionary)
            # flag = 0
            # if 'var' in line or 'div' in line or '.ir' in line or '.com' in line or 'width' in line:
            #     flag = 1
            # flag_1 = 0
            # for element in line.split(' '):
            #     for ele in english_alphabet:
            #         if ele in str(element) or str(element) == '':
            #             flag_1 = 1
            # if flag_1 == 0:
            #     terms.append(line.split(' '))
            # if flag == 0:


        # if terms != []:
        #     parag.append(terms)
        #     dict_term.append(parag)
    print("--- %s seconds ---" % (time.time() - start_time))
    return dictionary



# for item in stopwords_list():
#     stop_words.append(item)

# print(stopwords_list())


# wrong stop words !!!!!!!!!!!!!
def clear_dict():
    # clean stop words
    initial_state = extract_token()
    # for l in range(len(stop_words)):
    #     for i in range(len(initial_state)):
    #         for j in range(len(initial_state[i][1])):
    #             for k in range(len(initial_state[i][1][j])):
    #                 if stop_words[l] in initial_state[i][1][j][k]:
    #                     print('There is stop word in term' + str(initial_state[i][1][j][k]))
    #                     if str(initial_state[i][1][j][k]).split(str(stop_words[l]))[0] != '':
    #                         initial_state[i][1][j][k] = str(initial_state[i][1][j][k]).split(str(stop_words[l]))[0]
    #                         print('first' + str(initial_state[i][1][j][k]))
    #                     else:
    #                         initial_state[i][1][j][k] = str(initial_state[i][1][j][k]).split(str(stop_words[l]))[1]
    #                         print('second' + str(initial_state[i][1][j][k]))
    return initial_state


# defenitly true
# def terms_stemmer():
#     initial_state = [clear_dict()[0], clear_dict()[1]]
#     dictionary = []
#     lemmatizer = Lemmatizer()
#     stemmer = Stemmer()
#     for i in range(len(initial_state)):
#         for j in range(len(initial_state[i][1])):
#             for k in range(len(initial_state[i][1][j])):
#                 # print(initial_state[i][1][j][k])
#                 # if term appended to dictionary before
#                 flag = 0
#                 for l in range(len(dictionary)):
#                     if '#' in lemmatizer.lemmatize(initial_state[i][1][j][k]):
#                         print('# ! : ' + str(lemmatizer.lemmatize(initial_state[i][1][j][k])))
#                         if lemmatizer.lemmatize(initial_state[i][1][j][k]).split('#')[1] == dictionary[l][0]:
#                             dictionary[l][1] += 1
#                             dictionary[l][2].append(initial_state[i][0][0])
#                             flag = 1
#                             print('repeated noun term !' + str(stemmer.stem(initial_state[i][1][j][k])) + str(dictionary[l][1]) + str(dictionary[l][2]))
#                     elif stemmer.stem(initial_state[i][1][j][k]) == dictionary[l][0]:
#                         dictionary[l][1] += 1
#                         dictionary[l][2].append(initial_state[i][0][0])
#                         print('repeated verb term !' + str(stemmer.stem(initial_state[i][1][j][k])) + str(dictionary[l][1]) + str(dictionary[l][2]))
#                         flag = 1
#
#                 if flag == 0:
#                     if '#' in lemmatizer.lemmatize(initial_state[i][1][j][k]):
#                         print('new verb term 1 !' + str(initial_state[i][1][j][k]))
#                         print('new verb term 2 !' + str(lemmatizer.lemmatize(initial_state[i][1][j][k]).split('#')[1]) + '1' + str(initial_state[i][0][0]))
#                         dictionary.append([lemmatizer.lemmatize(initial_state[i][1][j][k]).split('#')[1], 1, [initial_state[i][0][0]]])
#                     else:
#                         print('new noun term 1 !' + str(initial_state[i][1][j][k]))
#                         dictionary.append([stemmer.stem(initial_state[i][1][j][k]), 1, [initial_state[i][0][0]]])
#                         print('new noun term 2 !' + str(
#                             lemmatizer.lemmatize(initial_state[i][1][j][k])) + '1' + str(
#                             initial_state[i][0][0]))
#     return dictionary


# print(terms_stemmer())


# print(clear_dict())

print(extract_token())
