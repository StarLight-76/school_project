from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Student, Teacher

def student_list(request):
    """Список всех учеников с их учителями"""
    # Используем prefetch_related для оптимизации запросов
    students = Student.objects.prefetch_related('teachers').all()
    return render(request, 'school_app/student_list.html', {'students': students})

def teacher_list(request):
    """Список всех учителей с их учениками"""
    teachers = Teacher.objects.prefetch_related('students').all()
    return render(request, 'school_app/teacher_list.html', {'teachers': teachers})