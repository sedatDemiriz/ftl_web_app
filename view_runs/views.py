# from django.template import loader
# from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import viewsets, permissions
from master_db.models import User_Submitted_Run as Run
from master_db.models import FTL_Ship as Ship
from view_runs.serializers import RunSerializer, ShipSerializer

class RunViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows User Submitted Runs to be viewed or edited
    """
    queryset = Run.objects.all()
    serializer_class = RunSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ShipViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FTL Ships to be viewed or edited
    """
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer
    # permission_classes = [permissions.IsAuthenticated]

# def index(request):
#     return HttpResponse('Hello world.')

# def user(request, username):
#     runs_for_user = Runs.objects.all().filter(username=username)
#     template = loader.get_template('view_runs/index.html')
#     context = {
#         'runs_for_user': runs_for_user,
#     }
#     return HttpResponse(template.render(context, request))

