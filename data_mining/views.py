from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def index(request):
    render(request, 'data_mining_templates.html')
