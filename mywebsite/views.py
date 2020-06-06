from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .forms import *
from .models import *
import os


def home(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        # try:
        #      send_mail("Message from " + from_name,
        #                contact_message + "\n\n\nSent by\n" + from_name + "\n" + from_email,
        #                from_email,
        #                [os.environ.get('EMAIL_RECEIVE')],
        #                fail_silently = False)
        # except BadHeaderError:
        #     pass
        return render(request, 'mywebsite/home.html', {'about':About.objects.all(), 
                                                    'education': Education.objects.all().order_by('-duration'), 
                                                    'projects':Project.objects.all(), 
                                                    'interests' : Interests.objects.all(),
                                                    'form': ContactForm()})

    return render(request, 'mywebsite/home.html', {'about':About.objects.all(), 
                                                    'education': Education.objects.all().order_by('-duration'), 
                                                    'projects':Project.objects.all(), 
                                                    'interests' : Interests.objects.all(),
                                                    'form': form})

def projects(request):
    return render(request, 'mywebsite/projects.html')
