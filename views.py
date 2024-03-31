from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from firstdjango.models import Emailsender
from pytube import *
from django.conf import settings
from django.core.mail import send_mail
def youtube(request):
    if request.method == 'POST': 
        url = request.POST['link'] 
        video = YouTube(url)  
        stream = video.streams.get_highest_resolution()
        stream.download() 
        return render(request, 'youtube.html') 
    return render(request, 'youtube.html')

def emailsender(request):
    if request.method=="POST":
        username = request.POST.get('name')
        email = request.POST.get('emailid')
        que=request.POST.get('ques')
        subject = 'Welcome to MyDjango'
        message = f'Hi {username}!!, Thank you for contacting us'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        email_sender=Emailsender(name=username,email=email,ques=que,date=datetime.today())
        email_sender.save()
    return render(request,"emailsender.html")
