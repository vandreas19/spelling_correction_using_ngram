#O
import re
from collections import Counter
import string
#%%
#%%
def read(file):
    return open(file).read()
#%%
def get_words(source):
    return re.findall(r'\w+', source.lower())
#%%
def get_unique_words(source):
    res = []
    for i in source:
        if i not in res:
            res.append(i)
    return res
#%%
def remove_punc(source):
    translator = str.maketrans('','', string.punctuation)
    for i in range(len(source)):
        source[i] = source[i].translate(translator)
        source[i] = ''.join([x for x in source[i] if not x.isdigit()])
    return source
#%%
def count_freq_each_word(source):
    return Counter(source)    
#%%
def gen_bigrams_indexing(source):
    uniq_gram = []
    for i in range(len(source)):
        for j in range(len(source[i])-1):
            kata = source[i][j:j+2]
            if kata not in uniq_gram:
                uniq_gram.append(kata)
    mydi = {}
    for i in uniq_gram: 
        lis = []
        for j in source:
            if i in j:
               lis.append(j)
        mydi[i] = lis
    return mydi
#%%
def searching(source, data):
    mydict = {} 
    indexing = gen_bigrams_indexing(data)
    for i in source:
        lis = []
        for j in range(len(i)-1):
            grams = i[j:j+2]
            if grams not in indexing:continue
            li_gram = indexing[grams]
            for q in li_gram:
                lis.append(q)
        co = dict(Counter(lis))
        mydict[i] = co
    return mydict
#%%
#jaccard coefficient
#return suggestion word if jaccard probability = 0,3
def reduct_suggestion_word_using_jaccard(source, data , key = 0.3):
    mydic = searching(source, data)
    res = {}
    for x,y in mydic.items():
        c1 = len(x) - 1
        lis = {}
        for i in y:
            c2 = len(i) - 1
            prob = (y[i]) / (y[i] + (c1 - y[i]) + (c2 - y[i]))
            if prob >= key:
                lis[i] = prob
        lis = sorted(lis.items(), key = lambda k : (k[1], k[0]), reverse = True)
        res[x] = lis
    return res
 
reads = read('SpellingCorrection/implementasi/big.txt')
data = get_words(reads)
data = remove_punc(data)
data_uniq = get_unique_words(data)


def main(query):
    li = [i for i in query.split(' ')]
    res = reduct_suggestion_word_using_jaccard(li, data_uniq)
    return res

 #%%
def indexing():
    w = gen_bigrams_indexing(data_uniq)
    w = sorted(w.items())
    return w

#TAMBAH

#%%