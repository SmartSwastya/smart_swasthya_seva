### tests.py
from django.test import TestCase
from .models import HomeModel

class HomeModelTest(TestCase):
    def test_create_home_model(self):
        home = HomeModel.objects.create(title='Test Title', content='Test Content')
        self.assertEqual(home.title, 'Test Title')