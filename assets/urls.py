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
]
