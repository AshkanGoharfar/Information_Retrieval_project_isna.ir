from __future__ import unicode_literals
from Create_inverted_index import *
from hazm import *

import numpy as np
import math

lemmatizer = Lemmatizer()
all_of_contents, inverted_index = extract_inverted_index()

######################### nan array for query words ###################################
# nan_array = []
# for i in range(len(query_words)):
#     nan_array.append(0)
#################### End #########################


docs_dict = {}

############ document dictionary for query's words ###################
# k = 0
# for i in range(len(query_words)):
#     if query_words[i] in inverted_index:
#         # print(inverted_index[query_words[i]]['doc'])
#         for j in range(len(inverted_index[query_words[i]]['doc'])):
#             if inverted_index[query_words[i]]['doc'][j] not in docs_dict:
#                 docs_dict[inverted_index[query_words[i]]['doc'][j]] = {'words': nan_array}
#             else:
#                 docs_dict[inverted_index[query_words[i]]['doc'][j]]['words'][k] += 1
#         k += 1
#         # docs_dict[inverted_index[query_words[i]]['doc']] = nan_array
############ End ###################


########################### bayad dictionary ijad konam ke key hash baraye har doc bashe va toosh bege har kalame chand bar tekrar shode
for i in range(len(merge_docs()['all_docs'])):
    nan_array = []
    for term in inverted_index:
        nan_array.append(0)
    docs_dict[i] = {'words': nan_array}

all_terms = []
k = 0
for term in inverted_index:
    # for j in range(len(inverted_index[term]['doc'])):
    #     # if inverted_index[term]['doc'][j] not in docs_dict:
    #     docs_dict[inverted_index[term]['doc'][j]]['words'][k] = 1
    #     # nan_array = []
    #     # for i in range(len(inverted_index)):
    #     #     nan_array.append(0)
    #     # nan_array[k] = 1
    #     # docs_dict[inverted_index[term]['doc'][j]] = {'words': nan_array}
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


# print(docs_dict)
# for doc in docs_dict:
#     for j in range(len(docs_dict[doc]['words'])):
#         if docs_dict[doc]['words'][j] > 0:
#

############################ last code of terms frequency in each doc
# k = 0
# for item in inverted_index:
#     # if query_words[i] in inverted_index:
#         # print(inverted_index[query_words[i]]['doc'])
#     for j in range(len(inverted_index[item]['doc'])):
#         if inverted_index[item]['doc'][j] not in docs_dict:
#             nan_array = []
#             for i in range(len(inverted_index)):
#                 nan_array.append(0)
#             nan_array[k] = 1
#             docs_dict[inverted_index[item]['doc'][j]] = {'words': nan_array, 'term': item}
#             # print('new doc in dict : ', docs_dict[inverted_index[item]['doc'][j]])
#         else:
#             docs_dict[inverted_index[item]['doc'][j]]['words'][k] += 1
#             # print('repeated doc in dict : ', docs_dict[inverted_index[item]['doc'][j]]['words'][k])
#     k += 1
#     # docs_dict[inverted_index[query_words[i]]['doc']] = nan_array


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


def calculate_tf_idf(term, doc, doc_coll):
    # tf_idf = 0
    print('Fucking length : ', len(docs_dict[doc]['words']))
    if term in inverted_index:
        print('selected document : ', doc)
        # print('term index : ', all_terms.index(term))
        tf = 1 + math.log10(docs_dict[doc]['words'][all_terms.index(term)])
        print('term frequency : ', inverted_index[term]['freq'])
        idf = math.log10(doc_coll / inverted_index[term]['freq'])
        tf_idf = tf * idf
        return tf_idf


print(calculate_tf_idf(list(inverted_index.keys())[0], 1, num_of_docs()))

# input("Search your query : ")
query = "صدا و سیما"
query_words = query.split(' ')

for item in query_words:
    if '#' in lemmatizer.lemmatize(item):
        # print('item before stemming : ', item)
        item = lemmatizer.lemmatize(item).split('#')[1]
        # print('item after stemming : ', lemmatizer.lemmatize(item).split('#')[1])


def score(document, query_words):
    score = 0
    # docs = 0
    # for documents in docs_dict:
    #     for query in query_words:
    #         if docs_dict[documents]['words'][all_terms.index(query)] != 0:
    #             print('This document contain this term : ', documents)
    # document = docs
    for term in query_words:
        # for i in range(len(list(docs_dict.keys()))):
        if docs_dict[int(document)]['words'][all_terms.index(term)] != 0:
            score += calculate_tf_idf(term, document, num_of_docs())
    return score


##################### result should use instad of 1 input for score function

print(inverted_index[query_words[0]]['doc'])

print(score(14, query_words))

# def calculate_tf_idf():
#     tf_idf = []
#     ############### calculate tf-idf for query's words ###################
#     # for i in range(len(query_words)):
#     #     word_tf = 0
#     #     for item in docs_dict:
#     #         # print(docs_dict[item]['words'][i])
#     #         if docs_dict[item]['words'][i] > 0:
#     #             word_tf += (1 + math.log10(docs_dict[item]['words'][i]))
#     #     print(num_of_docs())
#     #     print(inverted_index[query_words[i]]['freq'])
#     #     word_idf = num_of_docs() / inverted_index[query_words[i]]['freq']
#     #     tf_idf.append(word_tf - word_idf)
#     ############ calculate tf-idf for query's words ###################
#
#     # l = 0
#     # for elem in inverted_index:
#     #     word_tf = 0
#     #     for item in docs_dict:
#     #         # print(docs_dict[item]['words'][i])
#     #         if docs_dict[item]['words'][l] > 0:
#     #             # print('doc value', docs_dict[item]['words'][l])
#     #             word_tf += (1 + math.log10(docs_dict[item]['words'][l]))
#     #     # print(num_of_docs())
#     #     # print(inverted_index[elem]['freq'])
#     #     word_idf = num_of_docs() / inverted_index[elem]['freq']
#     #     tf_idf.append(word_tf - word_idf)
#     #     l += 1
#
#     l = 0
#     doc = list(docs_dict.keys())[0]
#     print('first doc : ', doc)
#     # for elem in docs_dict:
#     # doc = docs_dict.keys(0)
#
#     ######################## barresi e item haye dakhele iverted index va be kar girish shooon bara ye kolan invrted_index.keys(l) ?? !! ########
#     # all_term = list(inverted_index.keys())
#     doc_term = []
#     which_doc = 0
#     # print(docs_dict[list(docs_dict.keys())[which_doc]]['words'])
#     # print(docs_dict[list(docs_dict.keys())[1]]['words'])
#     for i in range(len(docs_dict[list(docs_dict.keys())[which_doc]]['words'])):
#         if docs_dict[list(docs_dict.keys())[which_doc]]['words'][i] > 0:
#             doc_term.append([list(inverted_index.keys())[i], i])
#     word_tf = 0
#     for term in doc_term:
#         for item in docs_dict:
#             print('word freq in each doc : ', docs_dict[item]['words'][term[1]])
#             ################## error !!!!!!!!!!!!!!
#             word_tf += (1 + math.log10(docs_dict[item]['words'][term[1]]))
#         print('sum of word_tf', word_tf)
#         word_idf = num_of_docs() / inverted_index[term[0]]['freq']
#         print('word_idf', word_idf)
#         print('each element word_tf - word_idf : ', word_tf - word_idf)
#         tf_idf.append(word_tf - word_idf)
#
#     # for item in doc_term:
#     #     if docs_dict[docs_dict.keys(0)]['word']
#     # word_tf = 0
#     # for item in docs_dict:
#     #     # print(docs_dict[item]['words'][i])
#     #     if docs_dict[item]['words'][l] > 0:
#     #         # print('doc value', docs_dict[item]['words'][l])
#     #         word_tf += (1 + math.log10(docs_dict[item]['words'][l]))
#     #     l += 1
#     # print(num_of_docs())
#     # print(inverted_index[elem]['freq'])
#
#     return tf_idf


# j = 0
# for i in range(len(query_words)):
#     if query_words[i] in inverted_index:
#         for k in range(len(inverted_index[query_words[i]]['doc'])):
#             if inverted_index[query_words[i]]['doc'][k] not in docs_dict:
#                 docs_dict[inverted_index[query_words[i]]['doc'][k]][j] = 1
#             else:
#                 docs_dict[inverted_index[query_words[i]]['doc'][k]][j] += 1
#         j += 1

# print(docs_dict)
