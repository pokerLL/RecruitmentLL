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
        Resume.objects.create(**data)
        return Response({})


class PictureViewSet(viewsets.ViewSet):
    def create(self, request):
        data = request.data.dict()
        picture = Picture.objects.create(**data)
        return Response({'id': picture.id})


class AttachmentViewSet(viewsets.ViewSet):
    def create(self, request):
        data = request.data.dict()
        attachment = Attachment.objects.create(**data)
        return Response({'id': attachment.id})


def upload(request):
    return JsonResponse({"1": "2"})
