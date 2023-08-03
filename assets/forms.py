from django import forms
from .models import Company, Employee, Device, DeviceLog


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


class DeviceCheckoutForm(forms.ModelForm):
    class Meta:
        model = DeviceLog
        fields = ['checked_out_by', 'checked_out_date', 'condition_at_checkout']


class DeviceReturnForm(forms.ModelForm):
    class Meta:
        model = DeviceLog
        fields = ['returned_date', 'condition_at_return']
