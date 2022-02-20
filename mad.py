import tweepy
consumer_key="nx8UZCofuS9fyZOTseBbQ3NIE"
consumer_secret="dKjlTFvz8T8GCwjj73LcDjUOYaqSFzecb9Hnxh9bEeRklNjNLr"
access_token="929321466574774273-8qDGKOWMNFlqaNsxHhSXFZJhWn0hpwC"
access_token_secret="TPh1YxWmItwJvloitwiavQatyolJ6LNHYwVTI7FPgbrMA"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

count=0

for tweet in public_tweets:
    count=count+1
    print("tweet #"+str(count)+"\n")
    print(tweet.text)
    print("-------------------------------------------------------------------")