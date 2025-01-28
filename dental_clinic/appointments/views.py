from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import AppointmentForm
from .models import Appointment
from django.contrib.auth.decorators import login_required

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