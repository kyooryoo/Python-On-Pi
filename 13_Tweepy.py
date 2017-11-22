import tweepy
# go to https://apps.twitter.com/ to setup your twitter app API
# keys and secrets below should be kept as secret and from your API
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""
# configure auth and access token
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth) # implement auth
# access a twitter user, modify it to your twitter user name for testing
user=api.get_user('twitter')
print "user name: "+str(user.screen_name)
print "# of followers: "+str(user.followers_count)
print "list of friends as follows:"
for friend in user.friends():
    print ">>"+str(friend.screen_name)
# netx line of code will post a new message to your twitter
# api.update_status('Hello World from Tweepy!')