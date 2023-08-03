from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    current_condition = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checked_out_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='checkouts')
    checked_out_date = models.DateTimeField()
    returned_date = models.DateTimeField(null=True, blank=True)
    condition_at_checkout = models.TextField()
    condition_at_return = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.device} - {self.checked_out_by}"
