from django.db import models
from .employee import Employee
from .computer import Computer

class EmployeeComputer(models.Model):
    """
    Creates the join table for the many to many relationship between computers and employees
    Author: Joe Shep
    methods: none
    """

    employee = models.ForeignKey(Employee, 
        related_name="EmployeeComputers",  
        null=True, # Makes column nullable in DB
        blank=True, # Allows blank value on objects
        on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer,  
        related_name="EmployeesComputer",  
        null=True, # Makes column nullable in DB
        blank=True, # Allows blank value on objects
        on_delete=models.CASCADE)
    assigned_date = models.DateField(null=True, auto_now=False, auto_now_add=False)
    unassigned_date = models.DateField(null=True, auto_now=False, auto_now_add=False)
    

