from rest_framework import serializers
from .models import Blogger

class BloggerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogger
        fields = ['url', 'time', 'title', 'body']
        time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")