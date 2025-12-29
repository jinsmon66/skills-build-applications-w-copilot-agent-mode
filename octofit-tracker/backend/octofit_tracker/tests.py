from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Team, User, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=10, distance=1.5)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=50)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')

    def test_user_email(self):
        self.assertEqual(self.user.email, 'test@example.com')

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Marvel')
        self.user = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=self.team)

    def test_api_root(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)

    def test_users_endpoint(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_teams_endpoint(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)
