from rest_framework import serializers
from .models import Team, User, Activity, Leaderboard, Workout


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model"""
    
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at', 'member_count']


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team', 'role', 'points', 'created_at']


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity model"""
    
    class Meta:
        model = Activity
        fields = [
            'id', 'user_id', 'user_email', 'user_name', 
            'activity_type', 'duration_minutes', 'distance_km',
            'calories', 'points', 'date', 'notes'
        ]


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serializer for Leaderboard model"""
    
    class Meta:
        model = Leaderboard
        fields = [
            'id', 'user_id', 'user_name', 'user_email',
            'team', 'points', 'rank', 'activities_count', 'last_updated'
        ]


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout model"""
    
    class Meta:
        model = Workout
        fields = [
            'id', 'name', 'description', 'category',
            'duration_minutes', 'difficulty', 'exercises'
        ]
