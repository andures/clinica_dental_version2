from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import AppointmentForm , PatientForm
from django.contrib.auth.decorators import login_required
from .models import Patient
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'appointments/home.html')

# create a register view
def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                login(request, form.save())
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'appointments/register.html', {'form': form})

# create a login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'appointments/login.html', {'form': form})

# create a logout view
def logout_view(request):
    logout(request)
    return redirect('home')

# create appointments view
@login_required
def Create_Appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.dentist = request.user
            appointment.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/Create_Appointment.html', {'form': form})

# create patients view
@login_required
def patients_list(request):
    patients = Patient.objects.filter(dentist=request.user)
    return render(request, 'appointments/patients_list.html', {'patients': patients})

# create patient create view
@login_required
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.dentist = request.user
            if patient.next_appointment:
                patient.next_appointment = timezone.make_aware(patient.next_appointment)
            patient.save()
            return redirect('patients_list')
        else:
            print(form.errors)
    else:
        form = PatientForm()
    return render(request, 'appointments/patient_form.html', {'form': form})

# create patient edit view
@login_required
def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk, dentist=request.user)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'appointments/patient_form.html', {'form': form})

# create patient delete view
@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk, dentist=request.user)
    if request.method == 'POST':
        patient.delete()
        return redirect('patients_list')
    return render(request, 'appointments/patient_confirm_delete.html', {'patient': patient})
