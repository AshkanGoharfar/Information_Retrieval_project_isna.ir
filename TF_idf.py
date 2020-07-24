from __future__ import unicode_literals
from Create_inverted_index import *
from hazm import *
import time
import numpy as np
import math

lemmatizer = Lemmatizer()
all_of_contents, inverted_index = extract_inverted_index()

all_terms = []
for term in inverted_index:
    all_terms.append(term)


def term_freq_in_all_doc():
    start_time = time.time()
    docs_dict = {}
    for i in range(len(merge_docs()['all_docs'])):
        nan_array = []
        for term in inverted_index:
            nan_array.append(0)
        docs_dict[i] = {'words': nan_array}
    for doc in range(len(docs_dict)):
        for j in range(len(all_of_contents[int(doc)])):
            docs_dict[doc]['words'][all_terms.index(all_of_contents[doc][j])] += 1
            # if all_of_contents[i][j] in docs_dict:

    # print('docs_dict : ')
    # for item in docs_dict:
    #     print(item)
    #     print(docs_dict[item]['words'])
    print("--- %s seconds ---" % (time.time() - start_time))
    return docs_dict


all_doc_term_freq = term_freq_in_all_doc()


def num_of_docs():
    num_of_doc = 0
    k = 0
    for item in merge_docs()['which_csv']:
        # print(merge_docs()['which_csv'][item]['end'])
        if k == len(merge_docs()['which_csv']) - 1:
            num_of_doc = merge_docs()['which_csv'][item]['end']
        k += 1
    return num_of_doc


# print('num of docs : ', num_of_docs())
docs_num = num_of_docs()
term_in_doc = []


def doc_tf_idf(doc):
    start_time = time.time()
    tf_idf = []
    # for i in range(len(all_terms)):
    #     tf_idf.append(0)
    # print('all_terms : ', len(all_terms))
    # print('inverted_index : ', len(inverted_index))
    # print('tf_idf : ', len(tf_idf))
    # print('Fucking length : ', len(all_doc_term_freq[doc]['words']))
    for term in inverted_index:
        # print('selected document : ', doc)
        # print('term index : ', all_terms.index(term))
        # print('tf : ', all_doc_term_freq[doc]['words'][all_terms.index(term)])
        if all_doc_term_freq[doc]['words'][all_terms.index(term)] > 0:
            tf = 1 + math.log10(all_doc_term_freq[doc]['words'][all_terms.index(term)])
            # print('term frequency : ', inverted_index[term]['freq'])
            idf = math.log10(docs_num / inverted_index[term]['freq'])
            # print('which tem : ', all_terms.index(term))
            # print('k : ', k)
            tf_idf.append(tf * idf)
        else:
            tf_idf.append(0)
        # print('counter : ', all_terms.index(term))
    print("--- %s seconds ---" % (time.time() - start_time))
    return tf_idf


# res = doc_tf_idf(1)
# print('calculate_tf_idf : ', res)
# print('len calculate_tf_idf : ', len(res))


def query_list(query_words):
    queries = []

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

    for i in range(len(inverted_index)):
        queries.append(0)
    for term in query_words:
        if term in all_terms and queries[all_terms.index(term)] == 0:
            queries[all_terms.index(term)] = 1
        if term in all_terms and queries[all_terms.index(term)] > 0:
            queries[all_terms.index(term)] += 1
    return queries


def query_tf_idf(queries):
    start_time = time.time()
    tf_idf = []
    # for i in range(len(all_terms)):
    #     tf_idf.append(0)
    # print('all_terms : ', len(all_terms))
    # print('inverted_index : ', len(inverted_index))
    # print('tf_idf : ', len(tf_idf))
    # print('Fucking length : ', len(all_doc_term_freq[doc]['words']))
    for term in inverted_index:
        # print('selected document : ', doc)
        # print('term index : ', all_terms.index(term))
        # print('tf : ', all_doc_term_freq[doc]['words'][all_terms.index(term)])
        if queries[all_terms.index(term)] > 0:
            tf = 1 + math.log10(queries[all_terms.index(term)])
            # print('term frequency : ', inverted_index[term]['freq'])
            idf = math.log10(docs_num / inverted_index[term]['freq'])
            # print('which tem : ', all_terms.index(term))
            # print('k : ', k)
            tf_idf.append(tf * idf)
        else:
            tf_idf.append(0)
        # print('counter for query : ', all_terms.index(term))
    print("--- %s seconds ---" % (time.time() - start_time))
    return tf_idf

#
#
# def score(document, query_words):
#     score = 0
#     for term in query_words:
#         if term_freq_in_all_doc()[int(document)]['words'][all_terms.index(term)] != 0:
#             score += calculate_tf_idf(term, document, num_of_docs())
#     return score
#
#
# for term in query_words:
#     for docs in term_freq_in_all_doc():
#         if term_freq_in_all_doc()[docs]['words'][all_terms.index(term)] != 0:
#             term_in_doc.append(docs)
#             print('which doc : ', docs)
#
# # print(inverted_index[query_words[0]]['doc'])
# suggest_doc = {}
# for best_doc in term_in_doc:
#     print('First best dock : ', best_doc)
#     score = score(int(best_doc), query_words)
#     if int(score) not in suggest_doc:
#         suggest_doc[int(score)] = best_doc
#         print('best_doc : ', best_doc)
#         print('score for best doc : ', score)
#
# print('suggest_doc : ', suggest_doc)
# sorted_suggest_doc = sorted(suggest_doc.items())
# print('sorted suggest doc : ', sorted_suggest_doc)
