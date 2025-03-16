from django.test import TestCase
from .models import AdminUser

class AdminUserTests(TestCase):
    def test_create_admin_user(self):
        user = AdminUser.objects.create(
            username="admin", email="admin@example.com", password="password123"
        )
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.email, "admin@example.com")
        self.assertEqual(user.password, "password123")
