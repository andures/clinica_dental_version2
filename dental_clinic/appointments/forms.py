from django import forms
from .models import Appointment, Patient

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'appointment_date', 'time', 'reason']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'conditions': forms.CheckboxSelectMultiple,
            'birth_date': forms.SelectDateWidget(years=range(1900, 2025)),
            'conditions_type': forms.RadioSelect(choices=Patient.CONDITIONS_TYPE_CHOICES),
        }