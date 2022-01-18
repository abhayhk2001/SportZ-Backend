from django.urls import path
from .views import adminviews
from .views import facultyviews
from .views import commonviews
from .views import studentviews


app_name = 'api'

urlpatterns = [
    # path('',adminviews.apiList, name="apiList"),
    # path('admin/login',adminviews.login, name="Admin Login"),
    # path('add/student',adminviews.addStudent, name="Add Student"),
    # path('add/faculty',adminviews.addFaculty, name="Add Faculty"),
    # path('add/event',adminviews.addEvent, name="Add Event"),
    # path('add/sportevent',adminviews.addSportEvent, name="Add Season Event"),
    # path('add/sportsteam',adminviews.addSportTeam, name="Add Sport Team"),
    # path('add/match',adminviews.addMatch, name="Add Match"),
    # path('updatematch',adminviews.updateMatch, name="Update Match"),
    path('admin/studentinfo', adminviews.adminStudentInfo,
         name="Admin Student Information"),
    path('admin/facultyinfo', adminviews.adminFacultyInfo,
         name="Admin Faculty Information"),
    path('admin/eventsinfo', adminviews.adminEventsInfo,
         name="Admin Events Information"),
    path('admin/matchesinfo', adminviews.adminMatchesInfo,
         name="Admin Matches Information"),
    path('admin/countinfo', adminviews.adminCountInfo,
         name="Admin Count Information"),


    # Admin and Faculty
    path('sportteaminfo', commonviews.sportTeamInfo,
         name="Sport Team Information"),


    # Faculty
    path('faculty/login', facultyviews.login, name="Faculty Login"),
    path('faculty/studentinfo', facultyviews.facultyStudentInfo,
         name="Faculty Student Information"),
    path('faculty/facultyinfo', facultyviews.facultyInfo,
         name="Faculty Information"),


    # Student
    path('student/login', studentviews.login, name="Student Login"),
    path('student/studentinfo', studentviews.studentInfo,
         name="Student Information"),
    path('student/sportteaminfo', studentviews.studentSportTeamInfo,
         name="Student Sport Team Information"),


    # Common
    path('matchinfo', commonviews.matchInfo, name="Match Information"),
    path('eventinfo', commonviews.eventInfo, name="Event Information"),
    path('sporteventinfo', commonviews.sportEventInfo,
         name="Sport Event Information"),

]
