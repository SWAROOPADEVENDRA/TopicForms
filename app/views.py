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

def display_topic(request):
    TOP=Topic.objects.all()
    d={'TOP':TOP}
    return render(request,'display_topic.html',d)


def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        tn=request.POST['tname']
        na=request.POST.get('name')
        url=request.POST['url']
        
        RTO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=RTO,name=na,url=url)[0]
        WO.save()
        return HttpResponse('Webpage create successfully')
    return render(request,'insert_webpage.html',d)

def display_webpage(request):
    WPDO=Webpage.objects.all()
    d={'WPDO':WPDO}
    return render(request,'display_webpage.html',d)

def insert_access(request):

    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    if request.method=='POST':
        na=request.POST['name']
        da=request.POST['date']
        au=request.POST['author']

        RTS=Webpage.objects.get(id=na)
        AO=AccessRecord.objects.get_or_create(name=RTS,date=da,author=au)[0]
        AO.save()
        return HttpResponse('Access record create successfully')
    
    return render(request,'insert_access.html',d)

def display_access(request):
    ARDO=AccessRecord.objects.all()
    d={'ARDO':ARDO}
    return render(request,'display_access.html',d)


def update_webpage(request):
    Webpage.objects.filter(name='Virat').update(name='Virat Kohili')
    Webpage.objects.filter(name='Virat').update(name='msd')
    WPDO=Webpage.objects.all()
    d={'WPDO':WPDO}
    return render(request,'display_webpage.html',d)

def delete_access(request):
    
    ARDO=AccessRecord.objects.all()
    AccessRecord.objects.filter(author='Virat kohili').delete()
    d={'ARDO':ARDO}
    return render(request,'display_access.html',d)