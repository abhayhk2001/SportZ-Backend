# Generated by Django 3.2.9 on 2021-12-10 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('name', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(default=None, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('dept', models.CharField(max_length=3)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('usn', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('dept', models.CharField(max_length=3)),
                ('semester', models.SmallIntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8)])),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SportsTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=15)),
                ('player', models.ManyToManyField(related_name='player', to='api.Student')),
                ('sports', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sport')),
            ],
        ),
        migrations.CreateModel(
            name='SportEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_team_event', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.event')),
                ('participants_ind', models.ManyToManyField(related_name='participant', to='api.Student')),
                ('participants_team', models.ManyToManyField(related_name='participants', to='api.SportsTeam')),
                ('sports', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sport')),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_team_event', models.BooleanField(default=False)),
                ('match_report', models.TextField()),
                ('won', models.IntegerField(choices=[(1, 1), (2, 2)])),
                ('held_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sportevent')),
                ('participant_ind_1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='participant1', to='api.student')),
                ('participant_ind_2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='participant2', to='api.student')),
                ('participant_team_1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='participant1', to='api.sportsteam')),
                ('participant_team_2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='participant2', to='api.sportsteam')),
            ],
        ),
    ]
