import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
path = '/home/rock/Bureau/rock_ML/TIPS_in_PY/tweeti.txt'
tweets_data = []

tweet_file = open(path, "r") #for opening the txt file in readable mode

for line in tweet_file:
        try:
                tweet = json.loads(line) #it's loading each line it encounters into in a json format
                tweets_data.append(tweet) #and feel this empty list by appending
        except:
                continue
              

tweets_feed = pd.DataFrame()
#lambda tweet: tweet['text'] this fction takes the object tweet and return the columns ['text'] inthis case ("es", "fr", "it","in")
#now, map applies those ("es", "fr", "it","in") to tweets_data (since "fr" is an elmt of components of tweets_data)
#list() brings out a list of just the languages
tweets_feed['text'] = list(map(lambda tweet:tweet['text'], tweets_data))
tweets_feed['lang'] = list(map(lambda tweet:tweet['lang'], tweets_data))
tweets_feed['user'] = list(map(lambda tweet:tweet['user'], tweets_data))
tweets_feed['location'] = list(map(lambda tweet: tweet['user']['location'] if tweet['user']['location'] != None else u'Unknown', tweets_data))
tweets_feed['followers_count'] = list( map(lambda tweet: tweet['user']['followers_count'], tweets_data))
tweets_feed['timestamp_ms'] = list(map(lambda tweet: tweet['timestamp_ms'], tweets_data))

tweets_by_lang = tweets_feed['lang'].value_counts()


fig,ax = plt.subplots()

ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of Tweets', fontsize=15)
ax.set_title('Top 5 Languages', fontsize=15, fontweight = 'bold')
tweets_by_lang[:5].plot(ax=ax,kind='bar', color ='red')
plt.show()
