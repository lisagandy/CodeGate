from django.db import models


class GateEvent(models.Model):
    name = models.CharField(max_length=20)


class TwitterUser(models.Model):    
    userID = models.CharField(max_length=15)
    userName = models.CharField(max_length=15)
    profileURL = models.URLField()
    location = models.CharField(max_length=30)
    numFollowers = models.IntegerField()


class Tweet(models.Model):
    gateKey = models.ForeignKey(GateEvent)
    tweetID = models.CharField(max_length=15)
    twitterUserKey = models.ForeignKey(TwitterUser)
    tweetText = models.CharField(max_length=140)
    tweetTime = models.DateTimeField()
    numRetweets = models.IntegerField(default=False)
    hasURL = models.BooleanField(default=False)
    hasHashTag = models.BooleanField(default=False)
    hasRetweet = models.BooleanField(default=False)
    tweetPlace = models.CharField(max_length=30)


class URL(models.Model):
    url = models.URLField()
    tweetKeys = models.ManyToManyField(Tweet)


class HashTag(models.Model):
    hashtag = models.CharField(max_length=20)
    tweetKey = models.ManyToManyField(Tweet)
    