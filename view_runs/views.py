from django.http import Http404
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as s
from rest_framework import generics
from rest_framework import mixins

from master_db.models import User_Submitted_Run as Run
from view_runs.serializers import RunSerializer as RS

class RunList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    test
    """
    queryset = Run.objects.all()
    serializer_class = RS

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, format=None):
        return self.create(request, *args, **kwargs)

class RunListDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    test2
    """
    queryset = Run.objects.all()
    serializer_class = RS

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

