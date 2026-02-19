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
from .views import (
    TeamViewSet, UserViewSet, ActivityViewSet,
    LeaderboardViewSet, WorkoutViewSet
)


@api_view(['GET'])
def api_root(request, format=None):
    """
    API root view that provides links to all available endpoints
    """
    return Response({
        'teams': reverse('team-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
        'admin': reverse('admin:index', request=request, format=format),
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
