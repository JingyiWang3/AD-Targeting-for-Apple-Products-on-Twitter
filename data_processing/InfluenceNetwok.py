
# coding: utf-8

# In[9]:

# Load packages
import pandas as pd
import numpy as np
import networkx as nx
import json
import operator
import pymongo
from pymongo import MongoClient



# Build network
def get_people(df):  # user_mentions screen_name 
    retweeted_index  = df.loc[df.retweeted_status.notnull(),:].index
    
    G = nx.DiGraph()
    group_dict = {}
    
    
    for i in range(df.shape[0]):
        # case 1: 发推人 at 了别人
        user =df.iloc[i].user.get('screen_name') #发推人
        user_mentions = df.iloc[i].entities.get('user_mentions')
        for i in range(len(user_mentions)):
            name = user_mentions[i]['screen_name'] 
            G.add_edge(user,name)
            group_dict[user] = 1
            group_dict[name] = 2
         # case 2: 发推人 转发了别人
        if i in retweeted_index:
            original_user = df.iloc[i].retweeted_status['user'].get('screen_name')
            G.add_edge(user,original_user)
            group_dict[original_user] = 3
            
        # case 3: 原 po at 了别人
            user_mentions2  = df.iloc[i].retweeted_status['entities'].get('user_mentions')
            if user_mentions2:
                for name in user_mentions2:
                    G.add_edge(user_mentions2, name['screen_name'])
                    group_dict[name] = 2
    return G,group_dict
        
        


# Page Rank

def get_page_rank(G,topN):
        
    page_rank = nx.pagerank(G, alpha = 0.85)
    sorted_pr = sorted(page_rank.items(),  key=operator.itemgetter(1), reverse=True)
    return pd.DataFrame(sorted_pr,columns = ['ScreenName',"PageRank"])

## In-degree
def get_indeg(G,first,last):
        
    indegCent = nx.in_degree_centrality(G)
    top_indegCent = sorted(indegCent.items(),  key=operator.itemgetter(1), reverse=True)[first:last]
    return indegCent,top_indegCent,pd.DataFrame(top_indegCent,columns = ['ScreenName',"In-degree"])

# TOP 10 influencer
def get_influencer(df):
    G,group_dict= get_people(df)
    indegCent,top6,top_indegCent = get_indeg(G,0,10)
    pr = get_page_rank(G,5)[0:10]
    new = pd.merge(pr,top_indegCent,how='inner', on='ScreenName' )
    return new

# plot graph
def get_subgraph(indegCent):
    sub_node =  [i[0] for i in indegCent]
    print(len(sub_node))
    for pairs in indegCent:
        [sub_node.append(i) for i in nx.all_neighbors(G,pairs[0])]
    print(len(sub_node))
    return (G.subgraph(sub_node ))
    

# data visualization
def get_d3_dict(subgraph,indegCent):
    mydict = {'nodes':[],'links':[]}
    for node in subgraph.nodes():
        ind_weight = indegCent[node]
        groups = group_dict[node]
        mydict['nodes'].append({"id":node, "group" : groups, "weight":ind_weight }) # tweets nodes :group1
        
    for edge in  subgraph.edges():
        mydict['links'].append({'source':edge[0], 'target':edge[1]})# edge betweens tweets and url  
    
    return mydict
        

# import json
# def writeToJSONFile(path, fileName, data):
#     filePathNameWExt = './' + path + '/' + fileName + '.json'
#     with open(filePathNameWExt, 'w') as fp:
#         json.dump(mydict, fp)

# writeToJSONFile('./','influence_dict',mydict)

