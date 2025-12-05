from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **kwargs):
        # Clear all data using pymongo for reliability with Djongo
        client = MongoClient()
        db = client.get_database('octofit_db')
        db.leaderboard.delete_many({})
        db.activity.delete_many({})
        db.workout.delete_many({})
        db.user.delete_many({})
        db.team.delete_many({})

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Team')
        dc = Team.objects.create(name='DC', description='DC Team')

        # Create Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel, is_superhero=True)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel, is_superhero=True)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc, is_superhero=True)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc, is_superhero=True)

        # Create Activities
        Activity.objects.create(user=tony, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='Swimming', duration=45, date=timezone.now().date())
        Activity.objects.create(user=clark, type='Flying', duration=60, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='Martial Arts', duration=50, date=timezone.now().date())

        # Create Workouts
        w1 = Workout.objects.create(name='Pushups', description='Upper body')
        w2 = Workout.objects.create(name='Situps', description='Core strength')
        w1.suggested_for.set([tony, steve])
        w2.suggested_for.set([clark, bruce])

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=clark, score=110)
        Leaderboard.objects.create(user=bruce, score=95)

        # Ensure unique index on email
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db.users.create_index([('email', 1)], unique=True)
        self.stdout.write(self.style.SUCCESS('Test data populated and unique index on email created.'))
