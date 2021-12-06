from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from api.models import Student, Admin, Faculty, Sport, SportsTeam, Event, SportEvent, Matches


class StudentCustomRegistrationSerializer(RegisterSerializer):
    seller = serializers.PrimaryKeyRelatedField(
        read_only=True,)  # by default allow_null = False
    usn = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    dept = serializers.CharField(required=True)
    semester = serializers.IntegerField(required=True)

    def get_cleaned_data(self):
        data = super(StudentCustomRegistrationSerializer,
                     self).get_cleaned_data()
        extra_data = {
            'usn': self.validated_data.get('usn', ''),
            'name': self.validated_data.get('name', ''),
            'dept': self.validated_data.get('dept', ''),
            'semester': self.validated_data.get('semester', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(StudentCustomRegistrationSerializer, self).save(request)
        user.is_student = True
        user.save()
        student = Student(student=user, usn=self.cleaned_data.get('usn'),
                          name=self.cleaned_data.get('name'),
                          dept=self.cleaned_data.get('dept'),
                          semester=self.cleaned_data.get('semester')),

        student.save()
        return user


class AdminCustomRegistrationSerializer(RegisterSerializer):
    admin = serializers.PrimaryKeyRelatedField(
        read_only=True,)  # by default allow_null = False
    name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super(AdminCustomRegistrationSerializer,
                     self).get_cleaned_data()
        extra_data = {
            'name': self.validated_data.get('name', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(AdminCustomRegistrationSerializer, self).save(request)
        user.is_admin = True
        user.save()
        admin = Admin(admin=user, name=self.cleaned_data.get('name'))
        admin.save()
        return user


class FacultyCustomRegistrationSerializer(RegisterSerializer):
    admin = serializers.PrimaryKeyRelatedField(
        read_only=True,)  # by default allow_null = False
    name = serializers.CharField(required=True)
    dept = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super(FacultyCustomRegistrationSerializer,
                     self).get_cleaned_data()
        extra_data = {
            'name': self.validated_data.get('name', ''),
            'dept': self.validated_data.get('dept', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(FacultyCustomRegistrationSerializer, self).save(request)
        user.is_faculty = True
        user.save()
        faculty = Faculty(faculty=user, name=self.cleaned_data.get(
            'name'), dept=self.cleaned_data.get('dept'))
        faculty.save()
        return user


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
