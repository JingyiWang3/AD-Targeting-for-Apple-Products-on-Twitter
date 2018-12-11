
# coding: utf-8

# In[ ]:


import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")


def get_retweet_df(twitterdf):
    influenceDF = pd.DataFrame()
    influenceDF['retweet_count'] = twitterdf.loc[twitterdf.retweeted_status.notnull(),'retweeted_status'].apply(lambda x: x['retweet_count'])
    influenceDF['followers_count'] = twitterdf.loc[twitterdf.retweeted_status.notnull(),'retweeted_status'].apply(lambda x: x['user']['followers_count'])
    influenceSeires = twitterdf.loc[twitterdf.retweeted_status.notnull(),'retweeted_status']
    influenceDF = pd.DataFrame(influenceSeires.tolist(),columns = ['text','retweet_count' ,'entities','extended_entities','lang','place',                                                               'favorite_count','reply_count'],                           index = influenceSeires.index.values)
    original_user = pd.DataFrame(twitterdf.loc[twitterdf.retweeted_status.notnull(),'retweeted_status'].apply(lambda x: x['user']).tolist(),             columns = ['id','name','followers_count'],index = influenceSeires.index.values)

    influenceDF = pd.concat([original_user,influenceDF],axis=1)
    entitiesDF = pd.DataFrame(influenceDF.entities.tolist())
    retweet =influenceDF[['text','name','retweet_count']]
    # retweet = pd.concat([retweet,entitiesDF],axis=0)
    retweet = retweet.groupby(['text','name']).max()
    retweet = retweet.sort_values('retweet_count',ascending  = False).reset_index() 
    return influenceDF,retweet


def get_entities(retweetNum,retweet,influenceDF):
    nrow = np.sum(retweet.retweet_count > retweetNum)
    print(nrow)
    specialtweets= []
    G = nx.Graph()
    mydict = {'nodes':[],'links':[]}
    for i in range(nrow):
        amount = retweet.retweet_count.iloc[i]
        temp = []
        try:
            tweet = retweet.text.iloc[i]
            G.add_node(amount,color = "lightblue")# blue or green
            dictionary = influenceDF.loc[influenceDF['text'].str.match(tweet),'entities'].any()
            weight = retweet.retweet_count.iloc[i]
            mydict['nodes'].append({"id":tweet,"group":1,"weight":weight}) 
            

            for (key, value) in dictionary.items():
                if value !=[]:
                    if key in ['media','urls','symbols']:  # url
                        [mydict['nodes'].append({"id":i['url'],"group":2}) for i in value]
                        [mydict['links'].append({'source':tweet,'target':i['url'],'value':1}) for i in value]   
                        temp.append([i['url'] for i in value])
                        [G.add_node(i['url'],color = "red") for i in value]
                        [G.add_edge(amount,j['url']) for j in value]
              
                    
                    
                    
                    elif key in ['hashtags']:  # yellow
                        [mydict['nodes'].append({"id":'#' + i['text'] ,"group":3}) for i in value]
                        [mydict['links'].append({'source':tweet,'target':'#'+i['text'],'value':1}) for i in value]   
                        temp.append(['#'+i['text'] for i in value])
                        [G.add_node('#'+i['text'],color = "yellow") for i in value]
                        [G.add_edge(amount,'#'+j['text']) for j in value]
                    
                    elif key in ['user_mentions']: # orange
                        [mydict['nodes'].append({"id":'@'+i['screen_name'],"group":4}) for i in value]
                        [mydict['links'].append({'source':tweet,'target':'@'+i['screen_name'],'value':1}) for i in value]
                        temp.append(['@'+i['screen_name'] for i in value])
                        [G.add_node('@'+i['screen_name'],color = "orange") for i in value]
        
                        [G.add_edge(amount,'@'+j['screen_name']) for j in value]
     
            if len(temp) == 2:
                for i in temp[0]:
                    for j in temp[1]:
                        mydict['links'].append({'source':i,'target':j,'value':1})
                        G.add_edge(i,j)
                         
        except:
            specialtweets.append(i)
 
    return mydict,temp,G



def draw_affinity_graph(df,name,retweetNum):
    influenceDF,retweet = get_retweet_df(df)
    mydict, temp ,G  = get_entities(retweetNum,retweet,influenceDF)
    node_color = [G.node[node]['color'] for node in G]
    pos=nx.spring_layout(G)
    nx.draw(G, node_size = 100,node_color = node_color,            edge_color = "grey",with_labels = True,font_size = 10)
    plt.gcf().set_size_inches(18.5, 10.5)
    plt.savefig('../output/' + name + 'Affinity.png', dpi=300)
    plt.show()


