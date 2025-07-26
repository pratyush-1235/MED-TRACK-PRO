from django.test import TestCase
from .models import User, Doctor, Patient, Appointment, Report

class HospitalModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass', role='Patient')
        self.doctor = Doctor.objects.create(user=self.user, specialization='Cardiology')
        self.patient = Patient.objects.create(user=self.user, age=30, gender='M')
        self.appointment = Appointment.objects.create(patient=self.patient, doctor=self.doctor, date='2023-10-01', time='10:00')
        self.report = Report.objects.create(patient=self.patient, document='report.pdf')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.role, 'Patient')

    def test_doctor_creation(self):
        self.assertEqual(self.doctor.specialization, 'Cardiology')

    def test_patient_creation(self):
        self.assertEqual(self.patient.age, 30)
        self.assertEqual(self.patient.gender, 'M')

    def test_appointment_creation(self):
        self.assertEqual(self.appointment.patient, self.patient)
        self.assertEqual(self.appointment.doctor, self.doctor)
        self.assertEqual(self.appointment.date, '2023-10-01')
        self.assertEqual(self.appointment.time, '10:00')

    def test_report_creation(self):
        self.assertEqual(self.report.patient, self.patient)
        self.assertEqual(self.report.document, 'report.pdf')