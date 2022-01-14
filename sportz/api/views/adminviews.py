from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from api.models import Admin, Student, Faculty, Matches, Event
from api.serializers import StudentSerializer, FacultySerializer, EventSerializer, MatchesSerializer


# Create your views here.
@api_view(['GET'])
def apiList(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)


@api_view(['GET'])
def adminFacultyInfo(request):
    serializer = FacultySerializer(Faculty.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def adminStudentInfo(request):
    serializer = StudentSerializer(Student.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def adminMatchesInfo(request):
    serializer = MatchesSerializer(Matches.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def adminEventsInfo(request):
    serializer = EventSerializer(Event.objects.all(),many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def login(request):
#     params = request.query_params.dict()
#     body = request.data.dict()
#     if(params['user'] != 'admin'):
#         return Response({'message':'Login User Error'})
#     success = True
#     try:
#         search = Admin.objects.get(username=body['username'], password=body['password'])
#     except:
#         success = False
#     if(not success):
#         response = {
#             'success': success,
#         }
#     else:
#         response = {
#             'user': 'admin-'+search.username,
#             'success': success,
#         }
#     return Response(response)

# @api_view(['POST'])
# def addStudent(request):
#     params = request.query_params.dict()
#     body = request.data.dict()
#     success = False
#     serializer = StudentSerializer(data=request.data)
#     if(serializer.is_valid()):
#         serializer.save()
#         success = True
#     response = {
#             'success': success,
#     }
#     return Response(response)

# @api_view(['POST'])
# def addFaculty(request):
#     params = request.query_params.dict()
#     body = request.data.dict()
#     api_urls = {
#         'Login': '/login',
#     }
#     return Response(api_urls)

# @api_view(['POST'])
# def addEvent(request):
#     params = request.query_params.dict()
#     body = request.data.dict()
#     api_urls = {
#         'Login': '/login',
#     }
#     return Response(api_urls)

# @api_view(['POST'])
# def addSportEvent(request):
#     params = request.query_params.dict()
#     body = request.data.dict()
#     api_urls = {
#         'Login': '/login',
#     }
#     return Response(api_urls)

# @api_view(['POST'])
# def addSportTeam(request):
#     params = request.query_params.dict()
#     body = request.data.dict()
#     api_urls = {
#         'Login': '/login',
#     }
#     return Response(api_urls)

# @api_view(['POST'])
# def addMatch(request):
#     params = request.query_params.dict()
#     body = request.data.dict()
#     api_urls = {
#         'Login': '/login',
#     }
#     return Response(api_urls)

# @api_view(['GET'])
# def updateMatch(request):
#     params = request.query_params.dict()
#     body = request.data.dict()
#     api_urls = {
#         'Login': '/login',
#     }
#     return Response(api_urls)
