from django.core.management.base import BaseCommand, CommandError
from news.models import NewsArticle
import urllib2
import time
import json
import math

import datetime, dateutil.parser



class Command(BaseCommand):
    """ Load NYTimes 'deflategate' articles

    """
    help = 'a script that loads NYTimes deflategate data for demo'

    def handle(self, *args, **options):
        request_string = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=deflategate&api-key=9f37a84046a643a827e9f24a47cb7f79%3A10%3A59379451"
        num_hits = float(json.loads(urllib2.urlopen(request_string).read())['response']['meta']['hits'])
    
        #headlines = []
        for i in xrange(0,int(math.ceil(num_hits/10.0))):
            request_string = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=deflategate&page={}&api-key=9f37a84046a643a827e9f24a47cb7f79%3A10%3A59379451".format(i)
            content = urllib2.urlopen(request_string).read()
            decoded = json.loads(content)
            
            print str(float(i * 10)/float(num_hits)) + "%"
            for j, story in enumerate(decoded['response']['docs']):
                d = dateutil.parser.parse(story['pub_date'])
                article = NewsArticle.objects.create_news_article(heading=story['headline']['main'], pub_date=d)
                if article:
                    article.save()