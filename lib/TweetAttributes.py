
# coding: utf-8

# ### Device or Operating System

# In[4]:


def sourceInfo(rawdata):
    
    # filter language
    rawdata = rawdata.loc[rawdata.lang =='en',:]
    

    data = rawdata.source.str.extractall(r'(?P<link>\<.+\>)(?P<text>.+)(<.+>)')
    source =  data.groupby('text').count().link 

    # # offical source
    offical = ['Twitter Web Client','Twitter for Android','Twitter for iPad','Twitter for iPhone','Other']

    source_mod = source.loc[source.index.isin(offical)]

    # # classify tweets from other sources as other

    other = pd.Series([source.loc[~source.index.isin(offical)].sum()], index=['Other'])
    source_mod = source_mod.append(other)
    return source_mod 

#sourceInfo(twitterdf)


# ### Tweets Language

# In[27]:


def lang(rawdata):
    lang = rawdata['lang'].value_counts()
    return lang
    
#lang(twitterdf)

