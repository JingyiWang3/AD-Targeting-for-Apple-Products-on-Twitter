
# coding: utf-8

# In[2]:


from __future__ import print_function
import tweepy
import json
import pymongo
from pymongo import MongoClient
import pandas as pd


# In[3]:


MONGO_HOST= 'mongodb://localhost/twitterdb'  # assuming you have mongoDB installed locally
                                             # and a database called 'twitterdb'


# In[4]:


KEYWORDS = ['keywords']


# In[5]:


CONSUMER_KEY = "  "
CONSUMER_SECRET = "  "
ACCESS_TOKEN = "  "
ACCESS_TOKEN_SECRET = "  "


# In[6]:


import json
import datetime
def preprocess_data(datajson, db):
  # Add More Information
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
     "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
     "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
     "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
     "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    post = datajson
    if str(post['user']['location']).split(', ')[-1] in states:
        device = ''
        if 'Android' in str(post['source']):
            device = 'Andriod'
        elif 'Web' in str(post['source']):
            device = 'Web'
        elif 'iPhone' in str(post['source']):
            device = 'iPhone'
        elif 'Buffer' in str(post['source']):
            device = 'Buffer'
        else:
            device = 'Others'
    
       # New DataFrame
        new_df = pd.DataFrame()
        new_df = new_df.append({'location' : str(post['user']['location']).split(', ')[-1], 
                                'time' : post['created_at'],
                                'tag' : 'iPad',
                                'device' : device,
                                'total_donations': 1},
                                ignore_index=True)

        a = new_df['time'].apply(lambda x: str(x).split(' '))
        a = a.apply(lambda x:x[2]+'-'+x[1]+'-'+x[5] + ' ' + x[3].split(':')[0] + ':' + x[3].split(':')[1] + ':00')
        new_df['time'] = a.apply(lambda x:datetime.datetime.strptime(x,'%d-%b-%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S') )
        ddf = new_df.rename(columns={'location': 'school_state',
                                     'time': 'date_posted',
                                     'tag': 'resource_type',
                                     'device': 'funding_status'})
       # Combine the jason
        datajsonn = ddf.to_dict('records')
        datajson.update(datajsonn[0])
    
        return datajson
      
    return None


# In[7]:


class StreamListener(tweepy.StreamListener):    
#This is a class provided by tweepy to access the Twitter Streaming API. 

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")
 
    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False
 
    def on_data(self, data):
        #This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
#             client = MongoClient(MONGO_HOST)
            
#             # Use twitterdb database. If it doesn't exist, it will be created.
#             db = client.twitterdb
            client = pymongo.MongoClient("mongodb+srv://username:password@cluster0-5mcg4.mongodb.net/twitterdb?retryWrites=true")
            db = client['twitterdb']['collection_name']
    
            # Decode the JSON from Twitter
            datajson = json.loads(data)
            
            datajson = preprocess_data(datajson,db)
            if datajson != None:
                db.insert_one(datajson)
    
        except Exception as e:
            print(e)


# In[ ]:


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) 
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(KEYWORDS))
streamer.filter(track=KEYWORDS)

