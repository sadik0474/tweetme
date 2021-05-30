from django.shortcuts import render
from django.http import Http404,HttpResponse


from .models import Tweet
# Create your views here.

def home_view(request,*args,**kwargs):
    return HttpResponse('Hello World')

def tweet_detail_view(request,tweet_id,*args,**kwargs):
    try:
        obj=Tweet.objects.get(id=tweet_id)
        if obj:
            return HttpResponse(f'Tweet:{tweet_id}: {obj.content}')
    except:
        raise Http404
    return HttpResponse('Hello World')