from __future__ import unicode_literals
import pandas as pd
from bs4 import BeautifulSoup as bs
from hazm import *
import time
from Generate_stop_words import *

stop_words = collect_stop_words()
which_csv = {}


def merge_docs():
    docs = ['ir-news-0-2.csv']
    all_content = []
    counter = 0
    for doc in docs:
        df = pd.read_csv(doc, delimiter=',')
        which_csv[doc] = {'start': counter, 'end': counter + len(df['content']) - 1}
        for i in range(len(df['content'])):
            all_content.append(df['content'][i])
        counter = len(df['content'])
    dict = {'which_csv': which_csv, 'all_docs': all_content}
    return dict


inverted_index = {}
contents = merge_docs()['all_docs']


def extract_inverted_index():
    start_time = time.time()
    lemmatizer = Lemmatizer()
    print(merge_docs()['which_csv'])
    for i in range(len(contents)):
        soup = bs(contents[i])
        text = soup.get_text()
        # parsing the text
        lines = text.splitlines()
        parag = []
        parag.append([i])
        for line in lines:
            # check if line has ':', if it doesn't, move to the next line
            if line.find(':') == -1:
                continue
            # Normalize each line
            normalizer = Normalizer()
            line = normalizer.normalize(line)
            for j in range(len(stop_words)):
                if stop_words[j] in line:
                    line = line.replace(stop_words[j], ' ')
                if '  ' in line:
                    line = line.replace('  ', ' ')
            for term in line.split(' '):
                flag = 0
                if '#' in lemmatizer.lemmatize(term) and lemmatizer.lemmatize(term).split('#')[
                    1] in inverted_index and i not in inverted_index[lemmatizer.lemmatize(term).split('#')[1]][
                    'doc']:
                    inverted_index[lemmatizer.lemmatize(term).split('#')[1]]['freq'] += 1
                    inverted_index[lemmatizer.lemmatize(term).split('#')[1]]['doc'].append(i)
                    flag = 1
                    # print('iterative verb : ' + str(lemmatizer.lemmatize(term).split('#')[1]) + str(inverted_index[lemmatizer.lemmatize(term).split('#')[1]]))
                elif term in inverted_index and i not in inverted_index[term]['doc']:
                    inverted_index[term]['freq'] += 1
                    inverted_index[term]['doc'].append(i)
                    flag = 1
                    # print('iterative noun : ' + str(term) + str(inverted_index[lemmatizer.lemmatize(term).split('#')[1]]))
                if flag == 0:
                    if '#' in lemmatizer.lemmatize(term) and lemmatizer.lemmatize(term) not in inverted_index:
                        inverted_index[lemmatizer.lemmatize(term).split('#')[1]] = {'freq': 1, 'doc': [i]}
                        # print('new verb : ' + str(lemmatizer.lemmatize(term).split('#')[1]) + str(inverted_index[lemmatizer.lemmatize(term).split('#')[1]]))

                    elif term != '' and term not in inverted_index:
                        inverted_index[term] = {'freq': 1, 'doc': [i]}
                        # print('new noun : ' + str(term) + str(inverted_index[term]))
        # print(inverted_index)
    print("--- %s seconds ---" % (time.time() - start_time))
    return inverted_index
