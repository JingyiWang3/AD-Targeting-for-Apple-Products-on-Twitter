
# coding: utf-8

# In[ ]:


import re
from bs4 import BeautifulSoup
# from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import RegexpTokenizer
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from nltk.stem.porter import PorterStemmer
from wordcloud import ImageColorGenerator
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")


def clean_text(text):
    lower= text.lower()
    pat = r'(at? @\w+)|(https?://[^ ]+)|(www.[^ ]+)'
    stripped = re.sub(pat, '', lower)
    negations_dic = {"isn't":"is not", "aren't":"are not", "wasn't":"was not", "weren't":"were not",
                    "haven't":"have not","hasn't":"has not","hadn't":"had not","won't":"will not",
                    "wouldn't":"would not", "don't":"do not", "doesn't":"does not","didn't":"did not",
                    "can't":"can not","couldn't":"could not","shouldn't":"should not","mightn't":"might not",
                    "mustn't":"must not"}
    neg_pattern = re.compile(r'\b(' + '|'.join(negations_dic.keys()) + r')\b')
    neg_handled = neg_pattern.sub(lambda x: negations_dic[x.group()], stripped)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(neg_handled)
    stemmer = PorterStemmer()
    stemmed =  [stemmer.stem(word) for word in tokens] # stemming
    stripped = [word for word in stemmed if word not in stopwords.words('english')]
    return(" ".join(stripped).strip())









def get_wordcloud(df,name):
    profile = df.user.apply(lambda x: x['description'])
    profile = profile.loc[profile.notnull()].reset_index(drop = True)
    profile = profile.apply(lambda x: clean_text(x))
    profile = profile.loc[profile.notnull()].reset_index(drop = True)
    text = " ".join(text for text in profile)

    # Load mask image
    twitter_mask = np.array(Image.open("./TwitterLogo.png"))

    # Create a word cloud image
    wordcloud = WordCloud(background_color="white",
                          font_path = 'CabinSketch-Bold.ttf',
                          max_words=400, 
                          mask= twitter_mask
                         ).generate(text)
    
    image_colors = ImageColorGenerator(twitter_mask)

    # Show word cloud
    plt.imshow(wordcloud.recolor(color_func=image_colors))
    plt.axis("off")
    plt.title('User Profile Word Cloud')
    plt.gcf().set_size_inches(18.5, 10.5)
    plt.savefig('../output/' + name + 'WordCloud.png', dpi=300)
    plt.show()

