from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def apiList(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)


@api_view(['POST'])
def login(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)

@api_view(['POST'])
def addStudent(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)

@api_view(['POST'])
def addFaculty(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)

@api_view(['POST'])
def addEvent(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)

@api_view(['POST'])
def addSportEvent(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)

@api_view(['POST'])
def addSportTeam(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)

@api_view(['POST'])
def addMatch(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)

@api_view(['GET'])
def updateMatch(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)


@api_view(['GET'])
def adminFacultyInfo(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)


@api_view(['GET'])
def adminStudentInfo(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)