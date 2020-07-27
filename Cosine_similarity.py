from Create_inverted_index import *
from TF_idf import *
from sklearn.metrics.pairwise import cosine_similarity
from operator import itemgetter

query = input("Search your query : ")
# query = "صدا و سیما"
query_words = query.split(' ')
queries = query_list(query_words)
merge_docs = merge_docs()
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


# print('query_list(query_words) : ', query_list(query_words))
# print('len query_list(query_words) : ', len(query_list(query_words)))
# print('great queries : ', query_tf_idf(queries))


def doc_contain_query(query_words):
    contained_doc = []
    for term in query_words:
        print(inverted_index[term]['doc'])
        for doc in inverted_index[term]['doc']:
            if doc not in contained_doc:
                contained_doc.append(doc)
    return contained_doc


docs_contain_query = doc_contain_query(query_words)
which_doc_tf_idf = doc_tf_idf(docs_contain_query[0])
queries_tf_idf = query_tf_idf(queries)

# which_exact_doc_tf_idf = []
# for i in range(len(which_doc_tf_idf)):


terms_tf_idf = []
for i in range(len(which_doc_tf_idf)):
    if which_doc_tf_idf[i] != 0:
        terms_tf_idf.append([i, which_doc_tf_idf[i]])

# print(cosine_similarity([which_doc_tf_idf], [queries_tf_idf]))
terms_tf_idf = sorted(terms_tf_idf, key=itemgetter(1), reverse=True)
print('Sorted terms_tf_idf : ', terms_tf_idf)

valuable_terms_in_doc = []
best_terms = [terms_tf_idf[0][0], terms_tf_idf[1][0], terms_tf_idf[2][0], terms_tf_idf[3][0], terms_tf_idf[4][0],
              terms_tf_idf[-5][0], terms_tf_idf[-4][0],
              terms_tf_idf[-3][0], terms_tf_idf[-2][0], terms_tf_idf[-1][0]]

doc_title = ""
for doc in docs:
    df = pd.read_csv(doc, delimiter=',')
    for i in range(len(merge_docs['all_title'])):
        if i == docs_contain_query[0]:
            doc_title = merge_docs['all_title'][i]

for i in range(len(best_terms)):
    valuable_terms_in_doc.append(all_terms[best_terms[i]])

output_1 = [doc_title, valuable_terms_in_doc]
print('output 1 : ', output_1)

# create champion list and output2
index_elimination = []
print('docs_contain_query len : ', len(docs_contain_query))
valuable_docs = []
for doc in docs_contain_query:
    value = 0
    word_counter = 0
    for word in query_words:
        value += all_doc_term_freq[doc]['words'][all_terms.index(word)]
        if all_doc_term_freq[doc]['words'][all_terms.index(word)] > 0:
            word_counter += 1
    valuable_docs.append([doc, value, word_counter])
# print('valuable_docs : ', valuable_docs)
valuable_docs_1 = sorted(valuable_docs, key=itemgetter(1), reverse=True)
valuable_docs_2 = sorted(valuable_docs, key=itemgetter(2), reverse=True)
print('valuable_docs_1 : ', valuable_docs_1)
# some_docs_contain_query
for i in range(10):
    print('valuable_docs_1[i][0] : ', valuable_docs_1[i][0])
    index_elimination.append(
        [valuable_docs_1[i][0], cosine_similarity([doc_tf_idf(valuable_docs_1[i][0])], [queries_tf_idf])[0][0]])
print('index_elimination : ', index_elimination)
index_elimination = sorted(index_elimination, key=itemgetter(1), reverse=True)
# index_elimination = sorted(index_elimination, key=itemgetter(1), reverse=True)
# for doc in docs
for i in range(10):
    print('Doc similarity to query value / which doc : ')
    print(index_elimination[i][1], index_elimination[i][0])
    df = pd.read_csv(docs[0], delimiter=',')
    print(merge_docs['all_title'][index_elimination[i][0]])
    print('Doc content : ')
    print(df['content'][index_elimination[i][0]])
    # valuable_terms_in_doc.append(all_terms[best_terms[i]])
