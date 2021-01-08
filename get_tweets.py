import csv
import re

# NOTE: static data from Trump Twitter Archive
def get_all_tweets():
	new_tweets = csv.DictReader(open("trump_tweet_2020.csv"))

	all_tweets = []

	for tweet in new_tweets:
		all_tweets.append(tweet['text'])
		print( "We've got %s tweets so far" % (len(all_tweets)) )
	return all_tweets

def clean_tweet(tweet):
    tweet = re.sub("https?\:\/\/", "", tweet)   #links
    tweet = re.sub("#\S+", "", tweet)           #hashtags
    tweet = re.sub("\.?@", "", tweet)           #at mentions
    tweet = re.sub("RT.+", "", tweet)           #Retweets
    tweet = re.sub("Video\:", "", tweet)        #Videos
    tweet = re.sub("\n", "", tweet)             #new lines
    tweet = re.sub("^\.\s.", "", tweet)         #leading whitespace
    tweet = re.sub("\s+", " ", tweet)           #extra whitespace
    tweet = re.sub("&amp;", "and", tweet) #encoded ampersand
    tweet = re.sub("&", "and", tweet)       #encoded ampersands
    return tweet

def write_tweets_to_csv(tweets):
    with open('tweets.csv', 'wb') as f:
        writer = csv.writer(f)
        for tweet in tweets:
            tweet = clean_tweet(tweet)
            if tweet:
                writer.writerow([tweet])

if __name__ == "__main__":
    tweets = get_all_tweets()
    write_tweets_to_csv(tweets)