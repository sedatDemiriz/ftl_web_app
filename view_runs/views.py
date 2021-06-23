# from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status as s

from master_db.models import User_Submitted_Run as Run
from view_runs.serializers import RunSerializer as RS

# class RunViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows User Submitted Runs to be viewed
#     """

#     queryset = Run.objects.all()
#     serializer_class = RunSerializer

@api_view(['GET', 'POST', ])
def get_post_runs(request, username, result):
    """
    test
    """
    if request.method == 'GET':
        runs = Run.objects.all().filter(username=username).filter(result=result)
        serializer = RS(runs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=s.HTTP_201_CREATED)
        return Response(serializer.errors, status=s.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', ])
def get_put_del_runs(request, pk):
    """
    test2
    """
    try:
        runs = Run.objects.get(pk=pk)
    except Run.DoesNotExist:
        return Response(status=s.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RS(runs)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RS(runs)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=s.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        runs.delete()
        return Response(status=s.HTTP_204_NO_CONTENT)