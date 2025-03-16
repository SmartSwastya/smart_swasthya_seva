from django.test import TestCase
from .models import Patient

class PatientTests(TestCase):
    def test_create_patient(self):
        patient = Patient.objects.create(
            first_name="Jane", last_name="Doe", date_of_birth="1990-01-01",
            email="jane.doe@example.com", phone_number="1234567890"
        )
        self.assertEqual(patient.first_name, "Jane")
        self.assertEqual(patient.last_name, "Doe")
        self.assertEqual(patient.email, "jane.doe@example.com")
        self.assertEqual(patient.phone_number, "1234567890")
