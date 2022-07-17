# Serializers define the API representation.
from jobs.models import Job,City,Resume
from rest_framework import serializers
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        depth = 2

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

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


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

