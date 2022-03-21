from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from api.models import Student, SportsTeam
from api.serializers import FacultySerializer, StudentSerializer

# Create your views here.


@api_view(['POST'])
def login(request):
    body = json.loads(request.body)
    success = True
    try:
        search = Student.objects.get(
            usn=body['username'], password=body['password'])
    except:
        success = False
    if(not success):
        response = {
            'success': success,
        }
    else:
        response = {
            'user': 'student-'+str(search.usn),
            'success': success,
        }
    return Response(response)


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
