"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
import os
from .views import (
    TeamViewSet, UserViewSet, ActivityViewSet,
    LeaderboardViewSet, WorkoutViewSet
)


@api_view(['GET'])
def api_root(request, format=None):
    """
    API root view that provides links to all available endpoints
    """
    # Get the CODESPACE_NAME from environment variable
    codespace_name = os.environ.get('CODESPACE_NAME')
    
    # Build the base URL based on environment
    if codespace_name:
        base_url = f'https://{codespace_name}-8000.app.github.dev'
    else:
        # Fallback to localhost for local development
        base_url = 'http://localhost:8000'
    
    return Response({
        'teams': f'{base_url}/api/teams/',
        'users': f'{base_url}/api/users/',
        'activities': f'{base_url}/api/activities/',
        'leaderboard': f'{base_url}/api/leaderboard/',
        'workouts': f'{base_url}/api/workouts/',
        'admin': f'{base_url}/admin/',
    })


# Create a router and register our viewsets
router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'users', UserViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
