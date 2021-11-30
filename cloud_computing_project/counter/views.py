from typing import Counter
from django.http.response import JsonResponse
from django.shortcuts import render
from .serializers import CounterSerializer
from .models import Counter

def increase_counter(request):
    c = Counter.objects.all().first()
    if c is None:
        c = Counter()
    c.value +=1
    c.save()
    return JsonResponse(c.value, safe=False, status=200)

def get_count(request):
    c = Counter.objects.all().first()
    return JsonResponse(c.value, safe=False, status=200)