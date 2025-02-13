from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import *


def student_index(request):
    students = Student.objects.all()
    context = {
        'students': students,
        'title': 'Students'
    }
    return render(request, 'students/student_index.html', context=context)


def kurs_index(request):
    kurs = Kurs.objects.all()
    context1 = {
        'kurs': kurs,
        'title': "Kurslar"
    }
    return render(request, 'kurs/kurs_index.html', context=context1)
