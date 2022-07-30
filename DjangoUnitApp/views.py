from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
#def index(request):
#    return HttpResponse("Listado de Estudiantes");

def index(request):
    context = {'clase':'Aprendiendo Django'}
    return render(request,'student_list.html',context)
