from django.urls import path
from . import views

urlpatterns = [
    # Companies
    path('companies/', views.company_list, name='company_list'),
    path('add_company/', views.add_company, name='add_company'),

    # Employees
    path('employees/', views.employee_list, name='employee_list'),
    path('add_employee/', views.add_employee, name='add_employee'),

    # Devices
    path('devices/', views.device_list, name='device_list'),
    path('add_device/', views.add_device, name='add_device'),
    path('device/<int:device_id>/checkout/', views.device_checkout, name='device_checkout'),
    path('device/<int:device_id>/return/', views.device_return, name='device_return'),

    # Companies
    path('api/companies/', views.CompanyListView.as_view(), name='api-company-list'),
    path('api/companies/<int:pk>/', views.CompanyDetailView.as_view(), name='api-company-detail'),

    # Employees
    path('api/employees/', views.EmployeeListView.as_view(), name='api-employee-list'),
    path('api/employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='api-employee-detail'),

    # Devices
    path('api/devices/', views.DeviceListView.as_view(), name='api-device-list'),
    path('api/devices/<int:pk>/', views.DeviceDetailView.as_view(), name='api-device-detail'),

    # Device Logs
    path('api/device-logs/', views.DeviceLogListView.as_view(), name='api-device-log-list'),
    path('api/device-logs/<int:pk>/', views.DeviceLogDetailView.as_view(), name='api-device-log-detail'),
]
