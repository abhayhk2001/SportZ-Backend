from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Faculty, Student, SportsTeam
from api.serializers import FacultySerializer, StudentSerializer


# Create your views here.
@api_view(['POST'])
def login(request):
    params = request.query_params.dict()
    body = request.data.dict()
    if(params['user'] != 'faculty'):
        return Response({'message': 'Login User Error'})
    success = True
    try:
        search = Faculty.objects.get(
            username=body['username'], password=body['password'])
    except:
        success = False
    if(not success):
        response = {
            'success': success,
        }
    else:
        response = {
            'user': 'faculty-'+search.id,
            'success': success,
        }
    return Response(response)


@api_view(['GET'])
def facultyStudentInfo(request):
    params = request.query_params.dict()
    body = request.data.dict()
    if(params['user'] not in ['faculty']):
        return Response({"success": False, 'message': 'User Error'})
    success = True
    serializer = StudentSerializer(SportsTeam.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def facultyInfo(request):
    params = request.query_params.dict()
    body = request.data.dict()
    if(params['user'] != 'faculty'):
        return Response({'message': 'Login User Error'})
    success = True
    try:
        search = Faculty.objects.get(
            username=int((body['token'].split('-'))[1]))
    except:
        success = False
    if(not success):
        response = {
            'success': success,
        }
    else:
        serializer = FacultySerializer(search)
    return Response(serializer.data)
