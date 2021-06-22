from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from master_db.models import User_Submitted_Run as Run
from view_runs.serializers import RunSerializer

class RunViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows User Submitted Runs to be viewed
    """

    queryset = Run.objects.all()
    serializer_class = RunSerializer

