from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/book/', views.book_appointment, name='book_appointment'),
    path('patients/<int:patient_id>/records/', views.patient_record, name='patient_record'),
    path('doctors/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]