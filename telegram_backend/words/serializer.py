from rest_framework import serializers
from words.models import Words


class WordSerializator(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ['pk', 'gender', 'word']