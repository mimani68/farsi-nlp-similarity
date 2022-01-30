from gensim.parsing.preprocessing import preprocess_string, lower_to_unicode, preprocess_documents, remove_stopwords, remove_short_tokens, split_alphanum, strip_multiple_whitespaces, strip_tags
from gensim.utils import deaccent, any2unicode, decode_htmlentities, tokenize, trim_vocab_by_freq
from hazm import *

f = open("dataset/marketing.txt", "r")
# f = open("dataset/example.txt", "r")
dataset = f.read()
# dataset = f.readlines()

f = open("farsi-stopword.txt", "r")
STOP_WORDS = f.read().split()

def farsi_preprocessing(rawDocument):
    tokenizedDocument = rawDocument.splitlines()

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
            print(tmp)


farsi_preprocessing(dataset)