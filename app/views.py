from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def htmlform(request):
    if request.method=='POST':
        return HttpResponse('post method is activated')

    return render(request,'htmlform.html')



def insert_topic(request):
    if request.method=='POST':
        to=request.POST['topic']
        tn=Topic.objects.get_or_create(topic_name=to)[0]
        tn.save()
        TOD=Topic.objects.all()
        d={'TOD':TOD}
        return render(request,'display_topic.html',d)

    return render(request,'insert_topic.html')



def inser_Webpage(request):
    tos=Topic.objects.all()
    d={'tos':tos}
    
    if request.method=='POST':
        topic=request.POST['topic']
        wn=request.POST['name']
        wu=request.POST['url']
        we=request.POST['email']
        To=Topic.objects.get(topic_name=topic)
        wo=Webpage.objects.get_or_create(topic_name=To,name=wn,url=wu,email=we)[0]
        wo.save()
        WOD=Webpage.objects.all()
        b={'WOD':WOD}

        return render(request,'display_webpage.html',b)

    return render(request,'inser_Webpage.html',d)



def insert_Accessrecord(request):
    WOS=Webpage.objects.all()
    d={'WOS':WOS}
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        wn=Webpage.objects.get(name=name)
        ar=AccessRecord.objects.get_or_create(name=wn,author=author,date=date)[0]
        ar.save()
        AOS=AccessRecord.objects.all()
        a={'AOS':AOS}
        return render(request,'display_accessrecord.html',a)

    return render(request,'insert_Accessrecord.html',d)
