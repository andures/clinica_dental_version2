from django import forms
from .models import Appointment, Patient


class AppointmentForm(forms.ModelForm):
    new_patient_name = forms.CharField(required=False, label="Nombre del Nuevo Paciente")
    new_patient_email = forms.EmailField(required=False, label="Correo Electrónico del Nuevo Paciente")
    new_patient_phone = forms.CharField(required=False, label="Teléfono del Nuevo Paciente")
    new_patient_age = forms.IntegerField(required=False, label="Edad del Nuevo Paciente")

    class Meta:
        model = Appointment
        fields = ['patient','email','appointment_date', 'time', 'reason']
    
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['patient'].queryset = Patient.objects.all()
        self.fields['email'].widget.attrs['readonly'] = True  # Hacer que el campo de correo sea de solo lectura

    def save(self, commit=True):
        instance = super(AppointmentForm, self).save(commit=False)
        if instance.patient:
            instance.email = instance.patient.email
        if commit:
            instance.save()
        return instance

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['dentist']
        widgets = {
            'conditions': forms.CheckboxSelectMultiple,
            'conditions_type': forms.RadioSelect(choices=Patient.CONDITIONS_TYPE_CHOICES),
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PatientForm, self).__init__(*args, **kwargs)
    
    def save(self, commit=True):
        instance = super(PatientForm, self).save(commit=False)
        if self.user:
            instance.dentist = self.user
        if commit:
            instance.save()
        return instance