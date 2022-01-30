from gensim import corpora, models, similarities
import jieba

f = open("dataset.txt", "r")
dataset = f.readlines()
keyword = 'مشتری توزیع کننده خرده فروش است'
texts = [jieba.lcut(text) for text in dataset]

dictionary = corpora.Dictionary(texts)
feature_cnt = len(dictionary.token2id)
corpus = [dictionary.doc2bow(text) for text in texts]
tfidf = models.TfidfModel(corpus)
kw_vector = dictionary.doc2bow(jieba.lcut(keyword))
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features = feature_cnt)
sim = index[tfidf[kw_vector]]

for i in range(len(sim)):
    if sim[i] > 0.9:
        # print('keyword is similar to text%d: %.2f' % (i + 1, sim[i]))
        print('==== %.2f ===' % sim[i])
        print(dataset[i])