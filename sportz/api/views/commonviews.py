from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def sportTeamInfo(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)

@api_view(['GET'])
def matchInfo(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)

@api_view(['GET'])
def eventInfo(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)

@api_view(['GET'])
def sportEventInfo(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)

