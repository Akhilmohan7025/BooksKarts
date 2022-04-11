
from django.db import models

# Create your models here.



class Employee(models.Model):
    emp_name=models.CharField(max_length=120)
    dept=models.CharField(max_length=120)
    email=models.EmailField(unique=True)
    salary=models.PositiveIntegerField()
    experience=models.PositiveIntegerField()
    active_status=models.BooleanField(default=True)


    def __str__(self):
        return self.email

# ORM queries
#
# CRUD Operation
# create
#     orm queries fo creating a new employee
#       emp=Employee(emp_name="abc",dept="abc",email"abc@gmail.com,salary=50000,experience=20)
#       emp.save()
# Retrieve
# orm queries for list all employees
#       emp=Employee.objects.all()
#       emp

# orm filtering
# orm queries for listing all employees whose dept is IT
#       emp=Employee.objects.filter(dept="IT")
#       emp

#orm filtering
# orm queries for all employees whose experience greater than 10.
#       emp=Employee.objects.filter(experience__gt=10)
#       emp

#orm filtering
# orm queries for listing all employees salary greater than 40000.
 #       emp=Employee.objects.filter(salary__gt=40000)
 #       emp

# orm filtering
# orm queries for listing all employees salary less than 40000.
#       emp=Employee.objects.filter(salary__lt=40000)
#       emp

# orm queries for listing all employees whose is greater than or equal to 45000.
#       emp=Employee.objects.filter(salary__gte=45000)
#       emp

# orm queries for listing all employees whose salary is greater than 20000 but less than 45000.
#       emp=Employee.objects.filter(salary__gt=20000,salary__lt=45000)
#       emp

# orm queries for listing all employees whose salary is greater than or equal to 30000 but less than 45000.
#       emp=Employee.objects.filter(salary__gte=30000,salary__lt=45000)
#       emp

# fetching object
#   orm queries for fetching a specific record using its id.
#       emp=Employee.objects.get(id=3)
#       emp



# update
# delete


