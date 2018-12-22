
# coding: utf-8

# In[1]:


import pymongo
from pymongo import MongoClient
import pandas as pd


# In[ ]:


def loaddata(product):
    client = pymongo.MongoClient("mongodb+srv://yh2866:Aa123456@cluster0-5mcg4.mongodb.net/tttest?retryWrites=true")
    cursor = client['twitterdb'][str(product)]
    df = pd.DataFrame(list(cursor.find()))
    return df

