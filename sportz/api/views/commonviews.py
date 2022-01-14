from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import SportsTeam, Matches,Event, SportEvent
from api.serializers import SportsTeamSerializer, MatchesSerializer, EventSerializer, SportEventSerializer
# Create your views here.
@api_view(['GET'])
def sportTeamInfo(request):
    params = request.query_params.dict()
    body = request.data.dict()
    if(params['user'] not in ['admin','faculty']):
        return Response({"success": False,'message':'User Error'})
    success = True
    serializer = SportsTeamSerializer(SportsTeam.objects.all(),many= True)
    return Response(serializer.data)

@api_view(['GET'])
def matchInfo(request):
    params = request.query_params.dict()
    body = request.data.dict()
    if(params['user'] not in ['admin','faculty','student']):
        return Response({"success": False,'message':'User Error'})
    success = True
    serializer = MatchesSerializer(Matches.objects.all(),many= True)
    return Response(serializer.data)

@api_view(['GET'])
def eventInfo(request):
    params = request.query_params.dict()
    body = request.data.dict()
    if(params['user'] not in ['admin','faculty','student']):
        return Response({"success": False,'message':'User Error'})
    success = True
    serializer = EventSerializer(Event.objects.all(),many= True)
    return Response(serializer.data)

@api_view(['GET'])
def sportEventInfo(request):
    params = request.query_params.dict()
    body = request.data.dict()
    if(params['user'] not in ['admin','faculty','student']):
        return Response({"success": False,'message':'User Error'})
    success = True
    serializer = SportEventSerializer(SportEvent.objects.all(),many= True)
    return Response(serializer.data)

