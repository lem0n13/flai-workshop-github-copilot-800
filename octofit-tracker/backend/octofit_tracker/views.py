from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Team, User, Activity, Leaderboard, Workout
from .serializers import (
    TeamSerializer, UserSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)


class TeamViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Team instances.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['created_at', 'member_count']


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing User instances.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'email']
    ordering_fields = ['points', 'created_at', 'name']
    filterset_fields = ['team', 'role']

    @action(detail=False, methods=['get'])
    def by_team(self, request):
        """Get users grouped by team"""
        team = request.query_params.get('team', None)
        if team:
            users = User.objects.filter(team=team)
            serializer = self.get_serializer(users, many=True)
            return Response(serializer.data)
        return Response({'error': 'Team parameter is required'}, status=400)


class ActivityViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Activity instances.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['user_name', 'activity_type']
    ordering_fields = ['date', 'points', 'duration_minutes']
    filterset_fields = ['activity_type', 'user_email']

    @action(detail=False, methods=['get'])
    def by_user(self, request):
        """Get activities for a specific user"""
        user_email = request.query_params.get('email', None)
        if user_email:
            activities = Activity.objects.filter(user_email=user_email)
            serializer = self.get_serializer(activities, many=True)
            return Response(serializer.data)
        return Response({'error': 'Email parameter is required'}, status=400)


class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for viewing Leaderboard (read-only).
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['rank', 'points']
    filterset_fields = ['team']

    @action(detail=False, methods=['get'])
    def top(self, request):
        """Get top N entries from leaderboard"""
        limit = int(request.query_params.get('limit', 10))
        leaderboard = Leaderboard.objects.all()[:limit]
        serializer = self.get_serializer(leaderboard, many=True)
        return Response(serializer.data)


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Workout instances.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']
    ordering_fields = ['duration_minutes', 'name']
    filterset_fields = ['category', 'difficulty']

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get workouts by category"""
        category = request.query_params.get('category', None)
        if category:
            workouts = Workout.objects.filter(category=category)
            serializer = self.get_serializer(workouts, many=True)
            return Response(serializer.data)
        return Response({'error': 'Category parameter is required'}, status=400)
