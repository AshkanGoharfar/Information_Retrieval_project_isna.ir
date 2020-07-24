from TF_idf import *
from sklearn.metrics.pairwise import cosine_similarity
# query = input("Search your query : ")
query = "صدا و سیما"
query_words = query.split(' ')
queries = query_list(query_words)

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


print(cosine_similarity([which_doc_tf_idf], [queries_tf_idf]))
