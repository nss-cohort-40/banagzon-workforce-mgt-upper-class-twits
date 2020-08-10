from django.db import models
# from django.urls import reverse
# from .department import Department

class Department(models.Model):

    department_name = models.CharField(max_length=100)
    department_budget = models.FloatField()
    

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")