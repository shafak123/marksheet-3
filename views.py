from django.shortcuts import render , redirect
from .forms import *
from .models import Student_marksheet
# Create your views here.

def index(request):
    return render (request, 'index.html')

def create_marksheet(request):
    if request.method == "POST":
        fom = Create_m(request.POST)
        fom.is_valid()
        fom.save()
        return redirect ("read")
    else:
        fom = Create_m()    
    return render (request, 'create_marksheet.html', {'create_marksheet' : Create_m})    

def read_marksheet(request):
    read = Student_marksheet.objects.all()
    return render (request, 'read_marksheet.html', {'read_marksheet' : read})

def delete_marksheet(request, id):
    if request.method == "POST":
        pi = Student_marksheet.objects.get(pk=id)
        pi.delete()
        return redirect('/')
    return render (request, 'delete_marksheet.html',)