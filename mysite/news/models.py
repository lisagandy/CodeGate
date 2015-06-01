from django.db import models
from django.core.exceptions import ObjectDoesNotExist


        
class NewsArticleManager(models.Manager):
    def create_news_article(self, heading, pub_date):
        try:
            e = NewsArticle.objects.get(heading=heading)
        except ObjectDoesNotExist:
            news_article = self.create(heading=heading, pub_date=pub_date)
            return news_article
        
        print("This news article already already exists!")
        return None


class NewsArticle(models.Model):
    heading = models.CharField(max_length=30)
    pub_date = models.DateTimeField()
    objects = NewsArticleManager()
    def __unicode__(self):
        return self.heading