from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    class Meta:
        model = User
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    suggested_for = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Workout
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = '__all__'
