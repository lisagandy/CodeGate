from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from news.models import NewsArticle


def index(request):
    latest_news_list = NewsArticle.objects.order_by('-pub_date')[:5]
    template = loader.get_template('beta/deflategate.html')
    context = RequestContext(request, {
        'latest_news_list': latest_news_list,
    })
    
    print latest_news_list
    return HttpResponse(template.render(context))