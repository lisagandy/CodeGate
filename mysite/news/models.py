from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class NewsArticleManager(models.Manager):
    def create_news_article(self, heading, url, pub_date, gate_term, source):
        try:
            e = NewsArticle.objects.get(heading=heading, pub_date=pub_date)
        except ObjectDoesNotExist:
            news_article = self.create(heading=heading, url=url, pub_date=pub_date, gate_term=gate_term, source=source)
            return news_article
        
        print("This news article already exists!")
        return None


class NewsArticle(models.Model):
    heading = models.CharField(max_length=30)
    url = models.URLField()
    pub_date = models.DateTimeField()
    gate_term = models.CharField(max_length=15)
    source = models.CharField(max_length=20)
    objects = NewsArticleManager()
    def __unicode__(self):
        return self.heading