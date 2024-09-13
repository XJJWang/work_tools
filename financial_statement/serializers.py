from .models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.Serializer):
    class Meta:
        model = Project
        fields = ['name', 'abbr', 'year'] 
