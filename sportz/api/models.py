from django.db import models
from django.conf import settings
sem_choices = (("1", "1"),		("2", "2"),		("3", "3"),		("4", "4"),
               ("5", "5"), 		("6", "6"), 		("7", "7"),		("8", "8"),	)


class Student(models.Model):
    usn = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=25)
    dept = models.CharField(max_length=3)
    semester = models.CharField(max_length=2, choices=sem_choices)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Admin(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=25)
    dept = models.CharField(max_length=3)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Sport(models.Model):
    sport_name = models.CharField(max_length=10)

    def __str__(self):
        return self.sport_name


class SportsTeam(models.Model):
    team_name = models.CharField(max_length=15)
    sports = models.ForeignKey(Sport, on_delete=models.CASCADE)
    player = models.ManyToManyField(Student, related_name="player")

    def __str__(self):
        return self.team_name


class Event(models.Model):
    name = models.CharField(max_length=15)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class SportEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    is_team_event = models.BooleanField(default=False)
    sports = models.ForeignKey(Sport, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    participants_team = models.ManyToManyField(
        SportsTeam, related_name="participants", blank=True)
    participants_ind = models.ManyToManyField(
        Student, related_name="participant", blank=True)

    def __str__(self):
        return self.event.name + " - " + self.sports.sport_name


class Matches(models.Model):
    held_in = models.ForeignKey(SportEvent, on_delete=models.CASCADE)
    is_team_event = models.BooleanField(default=False)
    participant_team_1 = models.ForeignKey(
        SportsTeam, on_delete=models.CASCADE, related_name="participant1", null=True, blank=True, default=0)
    participant_team_2 = models.ForeignKey(
        SportsTeam, on_delete=models.CASCADE, related_name="participant2", null=True, blank=True)
    participant_ind_1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="participant1", null=True, blank=True)
    participant_ind_2 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="participant2", null=True, blank=True)
    match_report = models.TextField()
    won = models.IntegerField(choices=((1, 1), (2, 2)))

    def __str__(self):
        return self.held_in.__str__() + ": Match - " + str(self.id)
