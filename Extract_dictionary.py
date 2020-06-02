from __future__ import unicode_literals

import pandas as pd
from bs4 import BeautifulSoup as bs

from hazm import *
from hazm import stopwords_list


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
            flag = 0
            if 'var' in line or 'div' in line or '.ir' in line or '.com' in line or 'width' in line:
                flag = 1
            if flag == 0:
                terms.append(line.split(' '))
        if terms != []:
            parag.append(terms)
            dict_term.append(parag)
    return dict_term


stop_words = ['»', '.', '. ', ' .', '«']

for item in stopwords_list():
    stop_words.append(item)

print(stopwords_list())


def clear_dict():
    initial_state = extract_token()
    for l in range(len(stop_words)):
        for i in range(len(initial_state)):
            for j in range(len(initial_state[i][1])):
                for k in range(len(initial_state[i][1][j])):
                    if stop_words[l] in initial_state[i][1][j][k]:
                        if str(initial_state[i][1][j][k]).split(str(stop_words[l]))[0] != '':
                            # print(initial_state[i][1][j][k])
                            initial_state[i][1][j][k] = str(initial_state[i][1][j][k]).split(str(stop_words[l]))[0]
                            # print(initial_state[i][1][j][k])
                        # else:
                        #     del(initial_state[i][1][j][k])
    return initial_state


print(clear_dict())
# print(extract_token())
