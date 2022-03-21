from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Student, Faculty, Matches, Event, SportEvent, Sport, Admin
from api.serializers import StudentSerializer, FacultySerializer, EventSerializer, MatchesSerializer, SportEventSerializer
from collections import OrderedDict
import json


# Create your views here.
@api_view(['GET'])
def apiList(request):
    api_urls = {
        'Login': '/login',
    }
    return Response(api_urls)


@api_view(['GET'])
def adminFacultyInfo(request):
    serializer = FacultySerializer(Faculty.objects.all().values(
        'username', 'name', 'dept'), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def adminStudentInfo(request):
    serializer = StudentSerializer(
        Student.objects.all().values('usn', 'name', 'dept', 'semester'), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def adminSportEventInfo(request):
    serializer = SportEventSerializer(
        SportEvent.objects.all(), many=True)
    raw = serializer.data
    if((raw[0])['is_team_event']):
        for i in range(len(raw)):
            raw[i].pop('is_team_event')
            raw[i].pop('participant_ind_1')
            raw[i].pop('participant_ind_2')
    else:
        for i in range(len(raw)):
            raw[i].pop('is_team_event')
            raw[i].pop('participants_team')
            raw[i].pop('participants_ind')
            raw[i]['event'] = Event.objects.get(
                id=raw[i]['event']).__str__()
            raw[i]['sports'] = Sport.objects.get(
                id=raw[i]['sports']).__str__()


@api_view(['GET'])
def adminMatchesInfo(request):
    serializer = MatchesSerializer(Matches.objects.all(), many=True)
    raw = serializer.data
    if((raw[0])['is_team_event']):
        for i in range(len(raw)):
            raw[i].pop('is_team_event')
            raw[i].pop('participant_ind_1')
            raw[i].pop('participant_ind_2')
    else:
        for i in range(len(raw)):
            raw[i].pop('is_team_event')
            raw[i].pop('participant_team_1')
            raw[i].pop('participant_team_2')
            raw[i]['participant_ind_1'] = Student.objects.get(
                usn=raw[i]['participant_ind_1']).name
            raw[i]['participant_ind_2'] = Student.objects.get(
                usn=raw[i]['participant_ind_2']).name
            raw[i]['held_in'] = SportEvent.objects.get(
                id=raw[i]['held_in']).__str__()
            raw[i]['won'] = raw[i]['participant_ind_'+str(raw[i]['won'])]
            raw[i].move_to_end('match_report')
            raw[i].move_to_end('won')
    return Response(raw)


@api_view(['GET'])
def adminEventsInfo(request):
    serializer = EventSerializer(Event.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def adminCountInfo(request):
    count = OrderedDict()
    count['events'] = Event.objects.all().count()
    count['matches'] = Matches.objects.all().count()
    count['students'] = Student.objects.all().count()
    count['sports'] = Sport.objects.all().count()
    return Response(count)


@api_view(['POST'])
def login(request):
    body = json.loads(request.body)
    success = True
    try:
        search = Admin.objects.get(
            username=body['username'], password=body['password'])
    except:
        success = False
    if(not success):
        response = {
            'success': success,
        }
    else:
        response = {
            'user': 'admin-'+str(search.username),
            'success': success,
        }
    return Response(response)
