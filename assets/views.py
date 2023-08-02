from django.shortcuts import render, redirect
from assets.models import Company, Employee, Device
from .forms import CompanyForm, EmployeeForm, DeviceForm


def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})


def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'add_company.html', {'form': form})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})


def device_list(request):
    devices = Device.objects.all()
    return render(request, 'device_list.html', {'devices': devices})


def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            device_id = form.cleaned_data['device_id']
            name = form.cleaned_data['name']
            serial_number = form.cleaned_data['serial_number']
            description = form.cleaned_data['description']

            device = Device(
                id=device_id,
                name=name,
                serial_number=serial_number,
                description=description,
            )

            device.save()
            return redirect('device_list')
    else:
        form = DeviceForm()
    return render(request, 'add_device.html', {'form': form})

