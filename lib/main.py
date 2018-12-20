
# coding: utf-8

# ### Load Data

# In[ ]:


from LoadData import loaddata

AirPods_df = loaddata('AirPods')
iPhone_df = loaddata('iPhone')
Watch_df = loaddata('Watch')
iPad_df = loaddata('iPad')


# ### Device or Operating System

# In[ ]:


from TweetAttributes import sourceInfo
sourceInfo(AirPods_df)


# In[ ]:


sourceInfo(iPhone_df)


# In[ ]:


sourceInfo(Watch_df)


# In[ ]:


sourceInfo(iPad_df)


# ### User Profile Word Cloud

# In[ ]:


from CreateWordCloud import get_wordcloud
get_wordcloud(AirPods_df, 'AirPods')


# In[ ]:


get_wordcloud(iPhone_df, 'iPhone')


# In[ ]:


get_wordcloud(Watch_df, 'Watch')


# In[ ]:


get_wordcloud(iPad_df, 'iPad')


# ### Tweet Sentiment Word Cloud

# In[ ]:


from SentimentAnalysis import get_sentiment
get_sentiment(AirPods_df, 'AirPods')


# In[ ]:


get_sentiment(iPhone_df, 'iPhone')


# In[ ]:


get_sentiment(Watch_df, 'Watch')


# In[ ]:


get_sentiment(iPad_df, 'iPad')


# ### LDA

# In[ ]:


from LDA import lda
import pyLDAvis.gensim
lda(AirPods_df, 'AirPods',4)


# In[ ]:


lda(iPhone_df, 'iPhone', 4)


# In[ ]:


lda(Watch_df, 'Watch',4)


# In[ ]:


lda(iPad_df, 'iPad', 4)


# ### Affinity

# In[ ]:


from getAffinitygraph import draw_affinity_graph, get_entities,get_retweet_df

influenceDF,retweet = get_retweet_df(AirPods_df)
mydict, temp ,G  = get_entities(200,retweet,influenceDF)
draw_affinity_graph(AirPods_df,'AirPods',200)


# In[ ]:


import json
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

writeToJSONFile('./','AirPods_aff',mydict)


# In[ ]:


influenceDF,retweet = get_retweet_df(iPhone_df)
mydict, temp ,G  = get_entities(200,retweet,influenceDF)
draw_affinity_graph(iPhone_df,'iPhone',200)


# In[ ]:


import json
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

writeToJSONFile('./','iphone_aff',mydict)


# In[ ]:


influenceDF,retweet = get_retweet_df(Watch_df)
mydict, temp ,G  = get_entities(100,retweet,influenceDF)
draw_affinity_graph(Watch_df,'Watch',100)


# In[ ]:


import json
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

writeToJSONFile('./','Watch_aff',mydict)


# In[ ]:


influenceDF,retweet = get_retweet_df(iPad_df)
mydict, temp ,G  = get_entities(200,retweet,influenceDF)
draw_affinity_graph(iPad_df,'iPad',200)


# In[ ]:


import json
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

writeToJSONFile('./','iPad_aff',mydict)

