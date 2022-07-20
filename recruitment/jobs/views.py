import json

from django.http import JsonResponse
# Create your views here.
from jobs.models import Job, City, Resume, Picture, Attachment
from jobs.serlizers import JobInfoSerializer, JobListSerializer, CitySerializer
from rest_framework import viewsets
from rest_framework.response import Response


class JobViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Job.objects.all()
        serializer = JobListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Job.objects.filter(id=pk)
        serializer = JobInfoSerializer(queryset, many=True)
        return Response(serializer.data)


class CityViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)


class ResumeViewSet(viewsets.ViewSet):
    def create(self, request):
        data = request.data.dict()
        data = json.loads(list((data.keys()))[0])
        obj = Resume.objects.create(**data)
        if obj:
            return Response({'id': obj.id})
        return Response({})


class PictureViewSet(viewsets.ViewSet):
    def create(self, request):
        data = request.data.dict()
        obj = Picture.objects.create(**data)
        if obj:
            return Response({'id': obj.id})
        return Response({})


class AttachmentViewSet(viewsets.ViewSet):
    def create(self, request):
        data = request.data.dict()
        obj = Attachment.objects.create(**data)
        if obj:
            return Response({'id': obj.id})
        return Response({})

