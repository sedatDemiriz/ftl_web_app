from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from master_db.models import User_Submitted_Run as Runs
# Create your views here.

def index(request):
    return HttpResponse('Hello world.')

def user(request, username):
    runs_for_user = Runs.objects.all().filter(username=username)
    template = loader.get_template('view_runs/index.html')
    context = {
        'runs_for_user': runs_for_user,
    }
    return HttpResponse(template.render(context, request))