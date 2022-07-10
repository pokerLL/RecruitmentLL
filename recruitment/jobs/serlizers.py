# Serializers define the API representation.
from jobs.models import Job
from rest_framework import serializers
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        depth = 2
class JobInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        exclude = ['creator']
        depth = 2

class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["id","job_name","job_type","job_city"]
        depth = 2


