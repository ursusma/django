from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from .models import Rank
from datetime import datetime

import urllib.request
import re

# Create your views here.

def index(request):
    
    def gettime():
        now = datetime.now().strftime('%Y-%m-%d')
        return now

    def geturl(url):
        a = urllib.request.Request(url)
        a.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36' '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
        dateurl = urllib.request.urlopen(a).read().decode('gbk')
        return gettext(dateurl)

    def gettext(dateurl):
        req = re.compile(r'title="(.*?)"\sdata="1\|1"\s.*href="(.*?)"')
        result = re.findall(req,dateurl)
        text_title =[]
        text_url = []
        text = [text_title,text_url]
        for g in result:
            text_title.append(g[0])
            text_url.append(g[1])
        return text

    def getdate(b):
        Rank.objects.all().delete()
        e = 1
        for i in range(0,10):
            Rank.objects.create(RankName=b[0][i],RankWeb=b[1][i],RankID=e)
            e += 1

    url = 'http://top.baidu.com'
    web = geturl(url)
    time = gettime()
    getdate(web)

    Ranks = Rank.objects.all()
    return render(request,'huiu/index.html',{'ranks':Ranks,'time':time})


def login(request):
    return render(request,'huiu/login.html')
