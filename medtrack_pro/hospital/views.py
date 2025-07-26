from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Appointment, Patient, Doctor, Report
from .forms import AppointmentForm, ReportForm

def register(request):
    if request.method == 'POST':
        # Handle user registration logic here
        pass
    return render(request, 'hospital/register.html')

def login_view(request):
    if request.method == 'POST':
        # Handle user login logic here
        pass
    return render(request, 'hospital/login.html')

@login_required
def patient_dashboard(request):
    patient = Patient.objects.get(user=request.user)
    appointments = Appointment.objects.filter(patient=patient)
    return render(request, 'hospital/patient_dashboard.html', {'appointments': appointments})

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = Patient.objects.get(user=request.user)
            appointment.save()
            return redirect('hospital:patient_dashboard')
    else:
        form = AppointmentForm()
    return render(request, 'hospital/book_appointment.html', {'form': form})

@login_required
def upload_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.patient = Patient.objects.get(user=request.user)
            report.save()
            return redirect('hospital:patient_dashboard')
    else:
        form = ReportForm()
    return render(request, 'hospital/upload_report.html', {'form': form})

@login_required
def doctor_dashboard(request):
    doctor = Doctor.objects.get(user=request.user)
    appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, 'hospital/doctor_dashboard.html', {'appointments': appointments})

@login_required
def admin_dashboard(request):
    doctors = Doctor.objects.all()
    appointments = Appointment.objects.all()
    return render(request, 'hospital/admin_dashboard.html', {'doctors': doctors, 'appointments': appointments})