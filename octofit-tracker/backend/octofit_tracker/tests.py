from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.assertEqual(str(team), 'Marvel')
    def test_create_user(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(name='Clark Kent', email='clark@dc.com', team=team, is_superhero=True)
        self.assertEqual(str(user), 'Clark Kent')
    def test_create_activity(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2025-12-05')
        self.assertEqual(str(activity), 'Tony Stark - Running')
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body')
        self.assertEqual(str(workout), 'Pushups')
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(name='Peter Parker', email='peter@marvel.com', team=team, is_superhero=True)
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(str(leaderboard), 'Peter Parker - 100')
