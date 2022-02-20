import tweepy
consumer_key="nx8UZCofuS9fyZOTsejiyhjjloBbQ3NIE"
consumer_secret="dKjlTFvz8T8GCwjj73LcDjUOYnjjhijhkknhionhaqSFzecb9Hnxh9bEeRklNjNLr"
access_token="929321466574774273-8qDGKOWMNFlqaNsxHhSXFZghji8uytfvbnmJhWn0hpwC"
access_token_secret="TPh1YxWmItwJvloitwiavQatyolJ6LNHsdfghjkoiuytredcvbnmkloYwVTI7FPgbrMA"

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
