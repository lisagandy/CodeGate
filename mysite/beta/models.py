from django.db import models

# Create your models here.
class GateEvent:
    name = models.CharField()

class Tweet:
    
    gateKey = models.ForeignKey(GateEvent)
    tweetID = models.CharField()
    twitterUserKey = models.ForeignKey(TwitterUser)
    tweetText = models.TextField()
    tweetTime = models.DateTimeField()
    numRetweets = models.IntegerField(default=0)
    hasURL = models.BooleanField()
    hasHashTag = models.BooleanField()
    hasRetweet = models.BooleanField()
    tweetPlace = models.CharField()
    
class URL:
    
    url = models.URLField()    
    tweetKeys = models.ManyToManyField(Tweet)
    
class HashTag:
    hashtag = models.CharField()
    tweetKey = models.ManyToManyField(Tweet)
    
class TwitterUser:
    
    userID = models.CharField()
    userName = models.CharField()
    profileURL = models.URLField()
    location = models.CharField()
    numFollowers = models.IntegerField()
    