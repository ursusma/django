from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.utils.encoding import smart_str

import urllib.request
import re
import os
import hashlib
import json
import requests
import traceback
import xml.etree.ElementTree as ET
import time

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

def status(request):

    def Cpustat():
        cpudate = os.popen('vmstat')
        cpufree = cpudate.read().split()
        cpufree = int(cpufree[-5]) + int(cpufree[-4])
        return cpufree

    def idlestat():
        idle = os.popen('vmstat')
        idledate = idle.read().split()
        idledate = idledate[-3]
        return idledate

    def Systime():
        time = datetime.now()
        return time

    def Usersnumber():
        usersnum = os.popen('uptime')
        usersdate = usersnum.read().split()
        usersdate = usersdate[5]
        return usersdate

    def Loadavg():
        f = open('/proc/loadavg')
        load = f.read()
        loadavg = load.split()
        loadavg = loadavg[0]
        f.close()
        return loadavg

    def Memoryfree():
        memory = open('/proc/meminfo')
        memorydate = memory.read().split()
        memorydate = memorydate[4]
        memory.close()
        return memorydate

    def signtime():
        sign = os.popen('uptime')
        signdate = sign.read().split()
        signdate = signdate[2]
        return signdate

    def date(a,b,c,d,e,f):
        Status.objects.all().delete()
        Status.objects.create(cpufree = a,idlestat = b, systime = c, usersnumber = d, loadavg = e, memoryfree = f)

    time = Systime()
    date(Cpustat(),idlestat(),signtime(),Usersnumber(),Loadavg(),Memoryfree())
    all = Status.objects.all()

    return render(request,'huiu/status.html',{'status':all,'time':time})

wxtoken = '******'
key = '******'
url = 'http://www.tuling123.com/openapi/api'

@csrf_exempt
def lnr(request):

    def get(request):
        signature = request.GET.get("signature","")
        timestamp = request.GET.get("timestamp","")
        nonce = request.GET.get("nonce","")
        echostr = request.GET.get("echostr","")
        token = wxtoken

        tmp_list = [token,timestamp,nonce]
        tmp_list.sort()
        tmp_str = tmp_list[0] + tmp_list[1] + tmp_list[2]
        tmpstr = hashlib.sha1(tmp_str.encode('utf-8')).hexdigest()

        if tmpstr == signature:
            return echostr
        else:
            return 'error'

    def getjson(recMsg):
        f = {"key":key,"info":recMsg}
        r = requests.post(url,data=f)
        resp = r.text
        if len(resp) == 0:
            return None
        js = json.loads(resp)
        if js['code'] == 100000:
            return js['text'].replace('<br>','\n')
        elif js['code'] == 200000:
            return js['url']
        else:
            return None

    def resplay(to,fr,con):
        ti = int(time.time())
        xmlForm = '''
            <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%d</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[%s]]></Content>
            </xml>
            '''%(to,fr,ti,con)
        return xmlForm

    def post(request):
        xmlData = ET.fromstring(request.body)

        touser = xmlData.find('ToUserName').text
        fromuser = xmlData.find('FromUserName').text
        msgtype = xmlData.find('MsgType').text
        content = xmlData.find('Content').text.encode('utf-8')

        aio = getjson(content)

        da = [touser,fromuser,msgtype,aio]

        if da[2] == 'text':
            to = da[1]
            fr = da[0]
            con = da[3]
            res = resplay(to,fr,con)
            return res
        

    if request.method == "GET":
        return HttpResponse(get(request))
    elif request.method == "POST":
        return HttpResponse(post(request))
