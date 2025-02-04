from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import AppointmentForm , PatientForm , BudgetForm
from django.contrib.auth.decorators import login_required
from .models import Patient, Appointment , Budget
from django.utils import timezone
import json
from django.http import JsonResponse
from django.db.models import Count , Sum

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

# dashboard view
@login_required
def dashboard(request):
    total_patients = Patient.objects.filter(dentist=request.user).count()
    total_appointments = Appointment.objects.filter(patient__dentist=request.user).count()
    upcoming_appointments = Appointment.objects.filter(patient__dentist=request.user, appointment_date__gte=timezone.now()).order_by('appointment_date')[:5]

    upcoming_appointments_json = json.dumps([
        {
            'patient': appointment.patient.name,
            'date': appointment.appointment_date.strftime('%Y-%m-%d'),
            'time': appointment.appointment_date.strftime('%H:%M'),
            'reason': appointment.reason
        }
        for appointment in upcoming_appointments
    ])

    # Obtener datos para los gráficos
    appointments_by_month = Appointment.objects.filter(patient__dentist=request.user).extra(select={'month': "strftime('%%m', appointment_date)"}).values('month').annotate(count=Count('id')).order_by('month')
    appointment_types = Appointment.objects.filter(patient__dentist=request.user).values('reason').annotate(count=Count('id')).order_by('-count')

    appointments_data = [0] * 12
    appointment_types_data = []
    appointment_types_labels = []

    for item in appointments_by_month:
        appointments_data[int(item['month']) - 1] = item['count']

    for item in appointment_types:
        appointment_types_labels.append(item['reason'])
        appointment_types_data.append(item['count'])

    context = {
        'total_patients': total_patients,
        'total_appointments': total_appointments,
        'upcoming_appointments': upcoming_appointments,
        'upcoming_appointments_json': upcoming_appointments_json,
        'appointments_data': json.dumps(appointments_data),
        'appointment_types_labels': json.dumps(appointment_types_labels),
        'appointment_types_data': json.dumps(appointment_types_data),
    }
    return render(request, 'appointments/dashboard.html', context)

# create appointment view
@login_required
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['new_patient_name']:
                # Crear un nuevo paciente
                patient = Patient.objects.create(
                    name=form.cleaned_data['new_patient_name'],
                    email=form.cleaned_data['new_patient_email'],
                    phone=form.cleaned_data['new_patient_phone'],
                    age=form.cleaned_data['new_patient_age'],
                    dentist=request.user
                )
            else:
                # Usar un paciente existente
                patient = form.cleaned_data['patient']
            
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.save()
            return redirect('appointments_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointment_form.html', {'form': form})

def get_patient_email(request, patient_id):
    patient=Patient.objects.get(id=patient_id)
    return JsonResponse({'email': patient.email})

# list appointments view
@login_required
def appointments_list(request):
    appointments = Appointment.objects.filter(patient__dentist=request.user)
    return render(request, 'appointments/appointments_list.html', {'appointments': appointments})

# edit appointment view
@login_required
def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, patient__dentist=request.user)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            if form.cleaned_data['new_patient_name']:
                # Crear un nuevo paciente
                patient = Patient.objects.create(
                    name=form.cleaned_data['new_patient_name'],
                    email=form.cleaned_data['new_patient_email'],
                    phone=form.cleaned_data['new_patient_phone'],
                    age=form.cleaned_data['new_patient_age'],
                    dentist=request.user
                )
            else:
                # Usar un paciente existente
                patient = form.cleaned_data['patient']
            
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.save()
            return redirect('appointments_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/appointment_form.html', {'form': form})

# delete appointment view
@login_required
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, patient__dentist=request.user)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointments_list')
    return render(request, 'appointments/appointment_confirm_delete.html', {'appointment': appointment})

@login_required
def budget_list(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id, dentist=request.user)
    budgets = Budget.objects.filter(patient=patient)

    if request.method == 'POST':
        budget_id = request.POST.get('budget_id')
        if budget_id:
            budget = get_object_or_404(Budget, pk=budget_id, patient=patient)
            form = BudgetForm(request.POST, instance=budget)
        else:
            form = BudgetForm(request.POST)
        
        if form.is_valid():
            budget = form.save(commit=False)
            budget.patient = patient
            budget.save()
            return redirect('budget_list', patient_id=patient.id)
    else:
        form = BudgetForm()

    total_cost = budgets.aggregate(total=Sum('cost'))['total'] or 0

    return render(request, 'appointments/budget_list.html', {
        'patient': patient,
        'budgets': budgets,
        'form': form,
        'total_cost': total_cost
    })
from django.http import JsonResponse

@login_required
def get_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk, patient__dentist=request.user)
    data = {
        'id': budget.id,
        'treatment': budget.treatment,
        'cost': budget.cost,
        'is_paid': budget.is_paid,
        'is_completed': budget.is_completed,
    }
    return JsonResponse(data)

@login_required
def budget_delete(request, pk):
    budget = get_object_or_404(Budget, pk=pk, patient__dentist=request.user)
    if request.method == 'POST':
        budget.delete()
        return redirect('budget_list', patient_id=budget.patient.id)
    return render(request, 'appointments/budget_confirm_delete.html', {'budget': budget})