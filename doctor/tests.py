from django.test import TestCase
from .models import Doctor

class DoctorTests(TestCase):
    def test_create_doctor(self):
        doctor = Doctor.objects.create(
            first_name="John", last_name="Doe", specialization="Cardiology",
            email="john.doe@example.com", phone_number="1234567890"
        )
        self.assertEqual(doctor.first_name, "John")
        self.assertEqual(doctor.last_name, "Doe")
        self.assertEqual(doctor.specialization, "Cardiology")
        self.assertEqual(doctor.email, "john.doe@example.com")
        self.assertEqual(doctor.phone_number, "1234567890")
