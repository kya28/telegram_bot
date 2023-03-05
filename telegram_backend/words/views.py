import random

from django.http import HttpResponseNotFound
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from words.models import Words
from words.serializer import WordSerializator


class RandomWord(APIView):
    def get(self, *args, **kwargs):
        all_words = Words.objects.all()
        random_word = random.choice(all_words)
        serializer_random_word = WordSerializator(random_word, many=False)
        return Response(serializer_random_word.data)


class NextWord(APIView):
    def get(self, request, pk, format=None):
        word = Words.objects.filter(pk__gt=pk).first()
        if not word:
            return HttpResponseNotFound()
        ser_word = WordSerializator(word, many=False)
        return Response(ser_word.data)



