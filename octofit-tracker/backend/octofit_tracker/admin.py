from django.contrib import admin
from .models import Team, User, Activity, Leaderboard, Workout


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin interface for Team model"""
    list_display = ['_id', 'name', 'member_count', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']
    ordering = ['name']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin interface for User model"""
    list_display = ['name', 'email', 'team', 'role', 'points', 'created_at']
    search_fields = ['name', 'email']
    list_filter = ['team', 'role', 'created_at']
    ordering = ['-points', 'name']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin interface for Activity model"""
    list_display = ['user_name', 'activity_type', 'duration_minutes', 'points', 'date']
    search_fields = ['user_name', 'user_email', 'activity_type']
    list_filter = ['activity_type', 'date']
    ordering = ['-date']
    date_hierarchy = 'date'


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin interface for Leaderboard model"""
    list_display = ['rank', 'user_name', 'team', 'points', 'activities_count', 'last_updated']
    search_fields = ['user_name', 'user_email']
    list_filter = ['team', 'last_updated']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin interface for Workout model"""
    list_display = ['name', 'category', 'difficulty', 'duration_minutes']
    search_fields = ['name', 'description']
    list_filter = ['category', 'difficulty']
    ordering = ['name']
