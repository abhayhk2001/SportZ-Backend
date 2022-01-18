from rest_framework import serializers

from api.models import Student, Admin, Faculty, Sport, SportsTeam, Event, SportEvent, Matches


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('usn', 'name', 'dept', 'semester')


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('username', 'name', 'dept')


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'


class SportsTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsTeam
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class SportEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportEvent
        fields = '__all__'


class MatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matches
        fields = '__all__'
