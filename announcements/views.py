from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from master_db.models import Community_Announcement as CA

# def index(request):
#     return HttpResponse('Hello world.')

def index(request):
    recent_announcements = CA.objects.all().order_by('-datetime')[:5]
    template = loader.get_template('announcements/index.html')
    context = {
        'recent_announcements': recent_announcements,
    }
    return HttpResponse(template.render(context, request))