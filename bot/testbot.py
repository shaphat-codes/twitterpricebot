import tweepy
import time


client = tweepy.Client(

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAM%2B%2BnwEAAAAA0I2DE79A6FzTs8z24a8H7Y4NpXs%3DhEXREMIs1iDjKiAO8jwEsiXgIBx1fdMcZDXwu5rFmmlThmQt8N',
consumer_key = 'xXmwd78qLUdgFPaVVxrvvPPSY',
consumer_secret = 'oU9wp96NYP4H6lRHD5PZiudVkzJhPr5xao5jEJ3XUsgGnctVRt',
access_token = '1156590259079172099-QXBnFhdfXdd1PlmJJbcMymjArkywlj',
access_token_secret = '9gqZgnpGBQWsKMVQ8GMD321JQIeDyeohmnzHkHdTbmo9R'

) 
auth = tweepy.OAuth1UserHandler('1iztkKfUoEeJZpEulTtyiYdln', 'JYSFagxOxD5KvWgzhfSag0iEMG76pnPgxPURqHj6bSPLXk8ECD', '1675806484028858368-L7Qys9xVDD5vQAgCks5lP1OC59d1PW', 'hsVEjY7NLp6qenBWzC0WolEXXep7YE2sHGC0JlLPzzWQw')
api = tweepy.API(auth) 

message = "your message has been received"
client_id = client.get_me().data.id
start_id = 1

while True:
    response = client.get_users_mentions(client_id, since_id=start_id)
    if response.data != None:
        for tweet in response.data:
            try:
                print(tweet.text)
                client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message)
                start_id = tweet.id
            except Exception as error:
                print(error)

    time.sleep(5)