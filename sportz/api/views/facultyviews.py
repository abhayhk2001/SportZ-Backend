from this import s
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Faculty, Student, SportsTeam, Event, Matches, Sport
from api.serializers import FacultySerializer, StudentSerializer, EventSerializer
import json
from collections import OrderedDict


# Create your views here.
@api_view(['POST'])
def login(request):
    body = json.loads(request.body)
    success = True
    try:
        print(body["username"])
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
            'user': 'faculty-'+str(search.id),
            'success': success,
        }
    return Response(response)


@api_view(['GET'])
def adminEventsInfo(request):
    serializer = EventSerializer(Event.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def facultyCountInfo(request):
    count = OrderedDict()
    count['events'] = Event.objects.all().count()
    count['matches'] = Matches.objects.all().count()
    count['students'] = Student.objects.all().count()
    count['sports'] = Sport.objects.all().count()
    return Response(count)


@api_view(['GET'])
def facultyStudentInfo(request):
    body = request.data
    try:
        user = body['token'].split("-")[0]
    except:
        return Response({"success": False, 'message': 'User Error'})
    if(user != 'faculty'):
        return Response({"success": False, 'message': 'User Error'})
    serializer = StudentSerializer(Student.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def facultyInfo(request):
    body = request.data
    try:
        user = body['token'].split("-")[0]
    except:
        return Response({"success": False, 'message': 'User Error'})
    if(user != 'faculty'):
        return Response({"success": False, 'message': 'User Error'})
    success = True
    try:
        search = Faculty.objects.get(
            username=(body['token'].split('-'))[1])
    except:
        success = False
    print(success)
    if(not success):
        response = {
            'success': success,
            'message': 'Faculty not Found'
        }
    else:
        serializer = FacultySerializer(search)
    return Response(serializer.data)
