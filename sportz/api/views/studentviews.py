from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['POST'])
def login(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)

@api_view(['GET'])
def studentInfo(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)


@api_view(['POST'])
def studentSportTeamInfo(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)