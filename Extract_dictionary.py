from __future__ import unicode_literals

import pandas as pd
from bs4 import BeautifulSoup as bs

from hazm import *
from hazm import stopwords_list

import string


english_alphabet = list(string.ascii_lowercase)
# print(english_alphabet)


def extract_token():
    df = pd.read_csv('ir-news-0-2.csv', delimiter=',')
    dict_term = []

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
            # flag = 0
            # if 'var' in line or 'div' in line or '.ir' in line or '.com' in line or 'width' in line:
            #     flag = 1
            flag_1 = 0
            for element in line.split(' '):
                for ele in english_alphabet:
                    if ele in str(element) or str(element) == '':
                        flag_1 = 1
            if flag_1 == 0:
                terms.append(line.split(' '))
            # if flag == 0:

        if terms != []:
            parag.append(terms)
            dict_term.append(parag)
    return dict_term


stop_words = ['»', '.', '. ', ' .', '«', '،', '۲۰۰']

for item in stopwords_list():
    stop_words.append(item)

# print(stopwords_list())


def clear_dict():
    # clean stop words
    initial_state = extract_token()
    for l in range(len(stop_words)):
        for i in range(len(initial_state)):
            for j in range(len(initial_state[i][1])):
                for k in range(len(initial_state[i][1][j])):
                    if stop_words[l] in initial_state[i][1][j][k]:
                        if str(initial_state[i][1][j][k]).split(str(stop_words[l]))[0] != '':
                            # print(initial_state[i][1][j][k])
                            if str(initial_state[i][1][j][k]).split(str(stop_words[l]))[0] != '':
                                initial_state[i][1][j][k] = str(initial_state[i][1][j][k]).split(str(stop_words[l]))[0]
                            else:
                                initial_state[i][1][j][k] = str(initial_state[i][1][j][k]).split(str(stop_words[l]))[1]
                            # print(initial_state[i][1][j][k])
                        # else:
                        #     del(initial_state[i][1][j][k])
    return initial_state


def terms_stemmer():
    initial_state = [clear_dict()[0], clear_dict()[1]]
    dictionary = []
    lemmatizer = Lemmatizer()
    stemmer = Stemmer()
    for i in range(len(initial_state)):
        for j in range(len(initial_state[i][1])):
            for k in range(len(initial_state[i][1][j])):
                # print(initial_state[i][1][j][k])
                # if term appended to dictionary before
                flag = 0
                for l in range(len(dictionary)):
                    if '#' in lemmatizer.lemmatize(initial_state[i][1][j][k]):
                        print('# ! : ' + str(lemmatizer.lemmatize(initial_state[i][1][j][k])))
                        if lemmatizer.lemmatize(initial_state[i][1][j][k]).split('#')[1] == dictionary[l][0]:
                            dictionary[l][1] += 1
                            dictionary[l][2].append(initial_state[i][0][0])
                            flag = 1
                            print('repeated noun term !' + str(dictionary[l][1]) + str(dictionary[l][2]))
                    elif stemmer.stem(initial_state[i][1][j][k]) == dictionary[l][0]:
                        dictionary[l][1] += 1
                        dictionary[l][2].append(initial_state[i][0][0])
                        print('repeated verb term !' + str(dictionary[l][1]) + str(dictionary[l][2]))
                        flag = 1

                if flag == 0:
                    if '#' in lemmatizer.lemmatize(initial_state[i][1][j][k]):
                        print('new verb term !' + str(lemmatizer.lemmatize(initial_state[i][1][j][k]).split('#')[1]) + '1' + str(initial_state[i][0][0]))
                        dictionary.append([lemmatizer.lemmatize(initial_state[i][1][j][k]).split('#')[1], 1, [initial_state[i][0][0]]])
                    else:
                        dictionary.append([stemmer.stem(initial_state[i][1][j][k]), 1, [initial_state[i][0][0]]])
                        print('new noun term !' + str(
                            lemmatizer.lemmatize(initial_state[i][1][j][k])) + '1' + str(
                            initial_state[i][0][0]))
    return dictionary


print(terms_stemmer())


# print(clear_dict())

# print(extract_token())
