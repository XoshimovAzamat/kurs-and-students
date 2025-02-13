from django.db import models
from django.template.defaultfilters import length

class Kurs(models.Model):
    title = models.CharField(max_length=50)
    start_time = models.CharField(max_length=10)
    finish_time = models.CharField(max_length=10)
    created_ed = models.DateTimeField(auto_now_add=True)
    update_ed = models.DateTimeField(auto_now=True)

class Student(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    email = models.CharField(max_length=50)
    kurs_id = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    created_ed = models.DateTimeField(auto_now_add=True)
    update_ed = models.DateTimeField(auto_now=True)

