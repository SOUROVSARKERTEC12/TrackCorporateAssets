from django.urls import path
from . import views

urlpatterns = [
    # Companies
    path('companies/', views.company_list, name='company_list'),
    path('add_company/', views.add_company, name='add_company'),
]
