from django.shortcuts import render, redirect
from assets.models import Company, Employee, Device, DeviceLog
from .forms import CompanyForm, EmployeeForm, DeviceForm, DeviceCheckoutForm, DeviceReturnForm


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


def device_checkout(request, device_id):
    device = Device.objects.get(pk=device_id)
    if request.method == 'POST':
        form = DeviceCheckoutForm(request.POST)
        if form.is_valid():
            checked_out_by = form.cleaned_data['checked_out_by']
            checked_out_date = form.cleaned_data['checked_out_date']
            condition_at_checkout = form.cleaned_data['condition_at_checkout']

            device_log = DeviceLog.objects.create(
                device=device,
                checked_out_by=checked_out_by,
                checked_out_date=checked_out_date,
                condition_at_checkout=condition_at_checkout,
            )

            device.assigned_to = checked_out_by
            device.current_condition = condition_at_checkout
            device.save()

            return redirect('device_list')
    else:
        form = DeviceCheckoutForm()
    return render(request, 'device_checkout.html', {'form': form, 'device': device})


def device_return(request, device_id):
    device = Device.objects.get(pk=device_id)
    if request.method == 'POST':
        form = DeviceReturnForm(request.POST)
        if form.is_valid():
            returned_date = form.cleaned_data['returned_date']
            condition_at_return = form.cleaned_data['condition_at_return']

            device_log = DeviceLog.objects.get(device=device, returned_date=None)
            device_log.returned_date = returned_date
            device_log.condition_at_return = condition_at_return
            device_log.save()

            device.assigned_to = None
            device.current_condition = condition_at_return
            device.save()

            return redirect('device_list')
    else:
        form = DeviceReturnForm()
    return render(request, 'device_return.html', {'form': form, 'device': device})
