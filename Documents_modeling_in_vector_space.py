from __future__ import unicode_literals
from Create_inverted_index import *
from hazm import *

import numpy as np
import math

lemmatizer = Lemmatizer()
all_of_contents, inverted_index = extract_inverted_index()

docs_dict = {}

for i in range(len(merge_docs()['all_docs'])):
    nan_array = []
    for term in inverted_index:
        nan_array.append(0)
    docs_dict[i] = {'words': nan_array}

all_terms = []
k = 0
for term in inverted_index:
    all_terms.append(term)
    k += 1


for doc in range(len(docs_dict)):
    for j in range(len(all_of_contents[int(doc)])):
        docs_dict[doc]['words'][all_terms.index(all_of_contents[doc][j])] += 1
        # if all_of_contents[i][j] in docs_dict:

print('docs_dict : ')
for item in docs_dict:
    print(item)
    print(docs_dict[item]['words'])


def num_of_docs():
    num_of_doc = 0
    k = 0
    for item in merge_docs()['which_csv']:
        # print(merge_docs()['which_csv'][item]['end'])
        if k == len(merge_docs()['which_csv']) - 1:
            num_of_doc = merge_docs()['which_csv'][item]['end']
        k += 1
    return num_of_doc


print('num of docs : ', num_of_docs())

term_in_doc = []


def calculate_tf_idf(term, doc, doc_coll):
    # print('Fucking length : ', len(docs_dict[doc]['words']))
    if term in inverted_index:
        # print('selected document : ', doc)
        # print('term index : ', all_terms.index(term))
        tf = 1 + math.log10(docs_dict[doc]['words'][all_terms.index(term)])
        # print('term frequency : ', inverted_index[term]['freq'])
        idf = math.log10(doc_coll / inverted_index[term]['freq'])
        tf_idf = tf * idf
        return tf_idf


print(calculate_tf_idf(list(inverted_index.keys())[0], 1, num_of_docs()))

# input("Search your query : ")
query = "صدا و سیما"
query_words = query.split(' ')

# Index elimination for multiple query
stop_words = collect_stop_words()
for word in query_words:
    if word in stop_words:
        query_words.remove(word)


for item in query_words:
    if '#' in lemmatizer.lemmatize(item):
        # print('item before stemming : ', item)
        item = lemmatizer.lemmatize(item).split('#')[1]
        # print('item after stemming : ', lemmatizer.lemmatize(item).split('#')[1])


def score(document, query_words):
    score = 0
    for term in query_words:
        if docs_dict[int(document)]['words'][all_terms.index(term)] != 0:
            score += calculate_tf_idf(term, document, num_of_docs())
    return score


for term in query_words:
    for docs in docs_dict:
        if docs_dict[docs]['words'][all_terms.index(term)] != 0:
            term_in_doc.append(docs)
            print('which doc : ', docs)

# print(inverted_index[query_words[0]]['doc'])
suggest_doc = {}
for best_doc in term_in_doc:
    print('First best dock : ', best_doc)
    score = score(int(best_doc), query_words)
    if int(score) not in suggest_doc:
        suggest_doc[int(score)] = best_doc
        print('best_doc : ', best_doc)
        print('score for best doc : ', score)

print('suggest_doc : ', suggest_doc)
sorted_suggest_doc = sorted(suggest_doc.items())
print('sorted suggest doc : ', sorted_suggest_doc)

