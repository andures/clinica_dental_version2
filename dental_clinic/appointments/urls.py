from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('patients/', views.patients_list, name='patients_list'),
    path('patients/create/', views.patient_create, name='patient_create'),
    path('patients/<int:pk>/edit/', views.patient_edit, name='patient_edit'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    path('patients/<int:patient_id>/budget/', views.budget_list, name='budget_list'),
    path('budget/<int:pk>/delete/', views.budget_delete, name='budget_delete'),
        path('budget/<int:pk>/get/', views.get_budget, name='get_budget'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('appointments/', views.appointments_list, name='appointments_list'),
    path('appointments/create/', views.appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/edit/', views.appointment_edit, name='appointment_edit'),
    path('appointments/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),
    path('get_patient_email/<int:patient_id>/', views.get_patient_email, name='get_patient_email'),
]
