from gensim import corpora, models, similarities
import jieba

from gensim.parsing.preprocessing import preprocess_string, lower_to_unicode, preprocess_documents, remove_stopwords, remove_short_tokens, split_alphanum, strip_multiple_whitespaces, strip_tags
from gensim.utils import deaccent, decode_htmlentities, tokenize, trim_vocab_by_freq
from hazm import *
from numpy import outer

f = open("dataset/marketing.txt", "r")
# f = open("dataset/example.txt", "r")
dataset = f.read()
# dataset = f.readlines()

f = open("farsi-stopword.txt", "r")
STOP_WORDS = f.read().split()

def FarsiPreprocessing(rawDocument):
    tokenizedDocument = rawDocument.splitlines()
    output = ''
    for i in range(len(tokenizedDocument)):
        if tokenizedDocument[i] is not "":

            normalizer = Normalizer()
            stemmer = Stemmer()
            lemmatizer = Lemmatizer()

            tokenizedDocument[i] = lower_to_unicode(tokenizedDocument[i], encoding='utf8', errors='strict')
            tokenizedDocument[i] = deaccent(tokenizedDocument[i])
            tokenizedDocument[i] = decode_htmlentities(tokenizedDocument[i])
            tokenizedDocument[i] = strip_tags(tokenizedDocument[i])
            tokenizedDocument[i] = strip_multiple_whitespaces(tokenizedDocument[i])
            tokenizedDocument[i] = split_alphanum(tokenizedDocument[i])
            tokenizedDocument[i] = remove_stopwords(tokenizedDocument[i], STOP_WORDS)

            # tokenizedDocument[i] = remove_short_tokens(tokenize(tokenizedDocument[i]), minsize=3)

            # tokenizedDocument[i] = preprocess_documents(tokenize(tokenizedDocument[i]))
            # CUSTOM_FILTERS = [lambda x: x.lower(), strip_tags, strip_punctuation]
            # tokenizedDocument[i] = preprocess_string(tokenizedDocument[i], CUSTOM_FILTERS))

            # tokenizedDocument[i] = trim_vocab_by_freq(dict(values=tokenizedDocument[i]), 5)
            # print(tokenizedDocument[i])

            tmp = normalizer.normalize(tokenizedDocument[i])
            tmp = stemmer.stem(tmp)
            tmp = lemmatizer.lemmatize(tmp)
            # print(tmp)
            output += '\n' + tmp
    return output


def findSimilarity(keyword: str, texts: str, matchPercentage: float, dictionary):
    dictionary = corpora.Dictionary(dictionary)
    feature_cnt = len(dictionary.token2id)
    corpus = [dictionary.doc2bow(text) for text in texts]
    tfidf = models.TfidfModel(corpus)
    kw_vector = dictionary.doc2bow(jieba.lcut(keyword))
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features = feature_cnt)
    sim = index[tfidf[kw_vector]]

    for i in range(len(sim)):
        if sim[i] > matchPercentage:
            print('==== %.2f ===' % sim[i])
            print(dataset[i])


if __name__ == "__main__":
    keyword = 'مشتری توزیع کننده خرده فروش است'

    f = open("dataset/marketing-preprocced.txt", "r")
    dictionary = FarsiPreprocessing(f.read())
    dictionary = [jieba.lcut(text) for text in dictionary.splitlines()]

    f = open("dataset/marketing.txt", "r")
    dataset = f.readlines()
    texts = [jieba.lcut(text) for text in dataset]

    findSimilarity(keyword, texts, 0.8, dictionary)