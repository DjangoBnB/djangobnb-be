from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def index(request):
    data = {'message': 'Hello, REST API!'}
    return Response(data)

@api_view(['GET'])
def detail(request):
    pass