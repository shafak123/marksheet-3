from django import forms
from .models import *


class Create_m(forms.ModelForm):
    class Meta:
        model = Student_marksheet
        fields = '__all__'


class Update_m(forms.ModelForm):
    class Meta:
        model = Student_marksheet
        fields = '__all__'        

       
