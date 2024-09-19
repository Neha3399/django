from django import forms
from django.db import models

# Create your models h
class Test(models.Model):
    title=models.CharField(max_length=30)
    discription=models.CharField(max_length=30)
    date=models.DateField()

class Department(models.Model):
    dept_name=models.CharField(max_length=10)
    def __str__(self):
        return self.dept_name

class Student(models.Model):
    name=models.CharField(max_length=15)
    Email=models.EmailField()
    dept=models.ForeignKey('Department',on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class  Todo(models.Model):
    title=models.CharField(max_length=15)
    discription=models.CharField(max_length=15)
    date_field=models.CharField(max_length=15)


