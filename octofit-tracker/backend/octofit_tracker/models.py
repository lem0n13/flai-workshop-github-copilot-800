from djongo import models
from django.utils import timezone


class Team(models.Model):
    """Team model for fitness tracking teams"""
    _id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    member_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class User(models.Model):
    """User model for fitness app users"""
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    role = models.CharField(max_length=50, default='member')
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.name} ({self.email})"


class Activity(models.Model):
    """Activity model for tracking user activities"""
    user_id = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_name = models.CharField(max_length=200)
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    calories = models.IntegerField()
    points = models.IntegerField()
    date = models.DateTimeField()
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'activities'
        ordering = ['-date']

    def __str__(self):
        return f"{self.user_name} - {self.activity_type} ({self.date})"


class Leaderboard(models.Model):
    """Leaderboard model for ranking users"""
    user_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    rank = models.IntegerField()
    activities_count = models.IntegerField()
    last_updated = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']

    def __str__(self):
        return f"#{self.rank} - {self.user_name} ({self.points} pts)"


class Exercise(models.Model):
    """Embedded model for exercises within workouts"""
    name = models.CharField(max_length=200)
    sets = models.IntegerField(null=True, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True


class Workout(models.Model):
    """Workout model for suggested workouts"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    difficulty = models.CharField(max_length=50)
    exercises = models.JSONField()

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return f"{self.name} ({self.difficulty})"
