from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def insert_topic(request):
    
    if request.method=='POST':
        tn=request.POST['tname']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic created successully')
    return render(request,'insert_topic.html')

def insert_webpage(request):

    if request.method=='POST':
        tn=request.POST['tname']
        na=request.POST.get('name')
        url=request.POST['url']
        
        RTO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=RTO,name=na,url=url)[0]
        WO.save()
        return HttpResponse('Webpage create successfully')
    return render(request,'insert_webpage.html')

def insert_access(request):
    if request.method=='POST':
        na=request.POST['name']
        da=request.POST['date']
        au=request.POST['author']

        RTS=Webpage.objects.get(name=na)
        AO=AccessRecord.objects.get_or_create(name=RTS,date=da,author=au)[0]
        AO.save()
        return HttpResponse('Access record create successfully')
    
    return render(request,'insert_access.html')