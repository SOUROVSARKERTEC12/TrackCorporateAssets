from django import forms
from .models import Company, Employee, Device


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'company']


class DeviceForm(forms.ModelForm):
    device_id = forms.IntegerField(label='Device ID')

    class Meta:
        model = Device
        fields = ['device_id', 'name', 'serial_number', 'description', 'assigned_to']


