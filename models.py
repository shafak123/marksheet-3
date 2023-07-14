from django.db import models

# Create your models here.

class Student_marksheet(models.Model):
    student_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    roll_number = models.IntegerField()
    school_code = models.IntegerField()
    data_of_birth = models.CharField(max_length=10)
    regular_or_private = models.CharField(max_length=15)
    section = models.CharField(max_length=1)
    hindi = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    so_science = models.IntegerField()
    sanskrit = models.IntegerField()
    science = models.IntegerField()
   
    






