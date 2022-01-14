from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['POST'])
def login(request):
    params = request.query_params.dict()
    body = request.data.dict()
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)

@api_view(['GET'])
def studentInfo(request):
    params = request.query_params.dict()
    body = request.data.dict()
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)


@api_view(['POST'])
def studentSportTeamInfo(request):
    params = request.query_params.dict()
    body = request.data.dict()
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)