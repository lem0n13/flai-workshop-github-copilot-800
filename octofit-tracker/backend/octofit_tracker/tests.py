from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Team, User, Activity, Leaderboard, Workout
from datetime import datetime


class TeamModelTest(TestCase):
    """Test cases for Team model"""

    def setUp(self):
        self.team = Team.objects.create(
            _id='test_team',
            name='Test Team',
            description='A test team',
            member_count=5
        )

    def test_team_creation(self):
        """Test team instance creation"""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.member_count, 5)
        self.assertEqual(str(self.team), 'Test Team')


class UserModelTest(TestCase):
    """Test cases for User model"""

    def setUp(self):
        self.user = User.objects.create(
            name='Test User',
            email='test@example.com',
            team='test_team',
            points=100
        )

    def test_user_creation(self):
        """Test user instance creation"""
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.points, 100)
        self.assertIn('Test User', str(self.user))


class ActivityModelTest(TestCase):
    """Test cases for Activity model"""

    def setUp(self):
        self.activity = Activity.objects.create(
            user_id='123',
            user_email='test@example.com',
            user_name='Test User',
            activity_type='running',
            duration_minutes=30,
            calories=300,
            points=25,
            date=datetime.now()
        )

    def test_activity_creation(self):
        """Test activity instance creation"""
        self.assertEqual(self.activity.activity_type, 'running')
        self.assertEqual(self.activity.duration_minutes, 30)
        self.assertEqual(self.activity.points, 25)


class WorkoutModelTest(TestCase):
    """Test cases for Workout model"""

    def setUp(self):
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='A test workout',
            category='strength',
            duration_minutes=45,
            difficulty='intermediate',
            exercises=[{'name': 'Push-ups', 'sets': 3, 'reps': 10}]
        )

    def test_workout_creation(self):
        """Test workout instance creation"""
        self.assertEqual(self.workout.name, 'Test Workout')
        self.assertEqual(self.workout.category, 'strength')
        self.assertEqual(self.workout.difficulty, 'intermediate')
        self.assertEqual(len(self.workout.exercises), 1)


class TeamAPITest(APITestCase):
    """Test cases for Team API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.team_data = {
            '_id': 'api_test_team',
            'name': 'API Test Team',
            'description': 'Team for API testing',
            'member_count': 3
        }
        self.team = Team.objects.create(**self.team_data)

    def test_get_teams_list(self):
        """Test retrieving list of teams"""
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_team_detail(self):
        """Test retrieving a single team"""
        url = reverse('team-detail', kwargs={'pk': self.team._id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'API Test Team')


class UserAPITest(APITestCase):
    """Test cases for User API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name='API Test User',
            email='apitest@example.com',
            team='test_team',
            points=50
        )

    def test_get_users_list(self):
        """Test retrieving list of users"""
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_user_detail(self):
        """Test retrieving a single user"""
        url = reverse('user-detail', kwargs={'pk': self.user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'apitest@example.com')


class ActivityAPITest(APITestCase):
    """Test cases for Activity API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.activity = Activity.objects.create(
            user_id='123',
            user_email='test@example.com',
            user_name='Test User',
            activity_type='cycling',
            duration_minutes=60,
            calories=600,
            points=50,
            date=datetime.now()
        )

    def test_get_activities_list(self):
        """Test retrieving list of activities"""
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)


class LeaderboardAPITest(APITestCase):
    """Test cases for Leaderboard API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.leaderboard_entry = Leaderboard.objects.create(
            user_id='123',
            user_name='Test Leader',
            user_email='leader@example.com',
            team='test_team',
            points=150,
            rank=1,
            activities_count=10
        )

    def test_get_leaderboard_list(self):
        """Test retrieving leaderboard"""
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)


class WorkoutAPITest(APITestCase):
    """Test cases for Workout API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.workout = Workout.objects.create(
            name='API Test Workout',
            description='Workout for API testing',
            category='cardio',
            duration_minutes=30,
            difficulty='beginner',
            exercises=[{'name': 'Jumping Jacks', 'sets': 3, 'reps': 20}]
        )

    def test_get_workouts_list(self):
        """Test retrieving list of workouts"""
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_workout_detail(self):
        """Test retrieving a single workout"""
        url = reverse('workout-detail', kwargs={'pk': self.workout.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'API Test Workout')


class APIRootTest(APITestCase):
    """Test cases for API root endpoint"""

    def setUp(self):
        self.client = APIClient()

    def test_api_root(self):
        """Test API root returns all endpoint links"""
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('teams', response.data)
        self.assertIn('users', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
