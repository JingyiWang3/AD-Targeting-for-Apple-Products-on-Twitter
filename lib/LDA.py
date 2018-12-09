
# coding: utf-8

# In[1]:


# Import data from mongodb
import pymongo
from pymongo import MongoClient
#MONGO_HOST= 'mongodb://localhost/twitterdb' 
#client = MongoClient(MONGO_HOST)
client = pymongo.MongoClient("mongodb+srv://fl2476:Aa123456@cluster0-5mcg4.mongodb.net/twitterdb?retryWrites=true")
db = client['twitterdb']['AirPods']
#db = client.twitterdb
cursor = db


# Save to a dataframe
import pandas as pd
twitterdf = pd.DataFrame(list(cursor.find()))


# ### LDA

# In[5]:


import nltk
nltk.download('punkt')
nltk.download('wordnet')
from TweetsCleaning import filter_tweet
from gensim import corpora, models, similarities
import os
import pandas as pd
#from collections import OrderedDict
import pyLDAvis.gensim

def lda(data, name):
    twitterdf = data.loc[data.lang == 'en',:]
    
    # to tower case + remove stop words
    clean = twitterdf.text.apply(lambda x: filter_tweet(x))

    # remove duplicated tweets
    cleaned = clean[~clean.apply(lambda x: ' '.join(word for word in x)).duplicated()]

    cleaned = cleaned.apply(lambda x: ' '.join(word for word in x))

    corpus=[]
    a=[]
    for i in range(len(cleaned)):
        a= cleaned.iloc[i]
        corpus.append(a)
        
    texts = [[word for word in str(document).lower().split()] for document in corpus]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]


    # lda model
    tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model
    corpus_tfidf = tfidf[corpus]  # step 2 -- use the model to transform vectors

    total_topics = 5
    lda = models.LdaModel(corpus, id2word=dictionary, num_topics=total_topics)
    corpus_lda = lda[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi

    #Show first n important word in the topics:
    #lda.show_topics(total_topics,5)

    pyLDAvis.enable_notebook()
    panel = pyLDAvis.gensim.prepare(lda, corpus_lda, dictionary, mds='tsne')
    pyLDAvis.save_html(panel, '../output/' + name + '-LDA.html')
    
    return panel
