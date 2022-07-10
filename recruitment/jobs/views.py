from django.shortcuts import render

# Create your views here.
from jobs.models import Job
from jobs.serlizers import JobInfoSerializer,JobListSerializer
from rest_framework.response import Response
from rest_framework import viewsets

class JobViewSet(viewsets.ViewSet):

    def list(self,request):
        queryset = Job.objects.all()
        serializer = JobListSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        queryset = Job.objects.filter(id=pk)
        serializer = JobInfoSerializer(queryset,many=True)
        return Response(serializer.data)
