from django.contrib import admin
from .models import Student, Faculty, Admin, Sport, SportsTeam, Event, SportEvent, Matches

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Admin)
admin.site.register(Sport)
admin.site.register(SportsTeam)
admin.site.register(Event)
admin.site.register(SportEvent)
admin.site.register(Matches)
