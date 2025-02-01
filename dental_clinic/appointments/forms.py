from django import forms
from .models import Appointment, Patient


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'appointment_date', 'time', 'reason']
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AppointmentForm, self).__init__(*args, **kwargs)


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