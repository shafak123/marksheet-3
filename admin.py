from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Student_marksheet)

class Student(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'mother_name', 'roll_number', 'school_code', 'data_of_birth', 'regular_or_private', 'section', 'hindi', 'english', 'maths', 'so_science', 'sanskrit', 'science']


