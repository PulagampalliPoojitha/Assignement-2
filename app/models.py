from django.db import models

# Create your models here.
class department(models.Model):
    dep_no=models.IntegerField(primary_key=True)
    dep_name=models.CharField(max_length=100)
    dep_location=models.CharField(max_length=100)



class employee(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    salary=models.IntegerField()
    dep_id=models.ForeignKey(department,on_delete=models.CASCADE)
