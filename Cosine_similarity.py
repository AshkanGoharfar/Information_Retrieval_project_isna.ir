from Create_inverted_index import *
from TF_idf import *
from sklearn.metrics.pairwise import cosine_similarity
from operator import itemgetter

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

terms_tf_idf = []
for i in range(len(which_doc_tf_idf)):
    terms_tf_idf.append([i, which_doc_tf_idf[i]])

print(cosine_similarity([which_doc_tf_idf], [queries_tf_idf]))
terms_tf_idf = sorted(terms_tf_idf, key=itemgetter(1), reverse=True)
print('Sorted terms_tf_idf : ', terms_tf_idf)

valuable_terms_in_doc = []
best_terms = [terms_tf_idf[0][0], terms_tf_idf[1][0], terms_tf_idf[2][0], terms_tf_idf[-3][0], terms_tf_idf[-2][0],
              terms_tf_idf[-1][0]]
for i in range(len(best_terms)):
    for doc in docs:
        df = pd.read_csv(doc, delimiter=',')
        # which_csv[doc] = {'start': counter, 'end': counter + len(df['content']) - 1}
        counter = len(df['content'])
        all_content = df['title'][docs_contain_query[0]]
    valuable_terms_in_doc.append(all_terms[best_terms[i]])

output_1 = [all_content, valuable_terms_in_doc]
print('output 1 : ', output_1)
