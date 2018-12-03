
# coding: utf-8

# In[ ]:


from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from TweetsCleaning import filter_tweet
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")

def get_cleaned_df(df):
    # to lower case + remove stop words
    clean = df.text.apply(lambda x: filter_tweet(x))

    # remove duplicated tweets
    cleaned = clean[~clean.apply(lambda x: ' '.join(word for word in x)).duplicated()]

    cleaned = cleaned.apply(lambda x: ' '.join(word for word in x))
    
    cleaned = pd.DataFrame(cleaned)
    
    return cleaned
    
    



def get_sentiment(df):
    
    cleaned = get_cleaned_df(df)
    cleaned['polarity'] = cleaned.apply(lambda x: TextBlob(x['text']).sentiment.polarity, axis=1)
    cleaned['subjectivity'] = cleaned.apply(lambda x: TextBlob(x['text']).sentiment.subjectivity, axis=1)
    text = " ".join(text for text in cleaned.text)
    
    def color_func(word, *args, **kargs):
        sentiment = cleaned.loc[cleaned.text.str.contains(word),'polarity'].mean()
        if sentiment < 0.00:
                colors = 'red'
        elif sentiment > 0.00:
                colors = 'green'
        else:
                colors = 'yellow'
        return colors

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
    plt.imshow(wordcloud.recolor(color_func=color_func))
    plt.axis("off")
    plt.gcf().set_size_inches(18.5, 10.5)

    plt.savefig('../output/SentimentWC.png', dpi=300)
    plt.show()
    

