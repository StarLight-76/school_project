from django.shortcuts import render
from django.db import connection
from .models import Student, Teacher

# Задание 1 (основное)
def student_list(request):
    """
    Список учеников с оптимизацией через prefetch_related (ЗАДАНИЕ 2).
    """
    students = Student.objects.prefetch_related('teachers').all()
    return render(request, 'school_app/student_list.html', {'students': students})

def teacher_list(request):
    """
    Список учителей с их учениками (используем related_name='students').
    """
    teachers = Teacher.objects.prefetch_related('students').all()
    return render(request, 'school_app/teacher_list.html', {'teachers': teachers})


# Задание 2 (дополнительное)
def student_list_with_analysis(request):
    """
    Страница для анализа SQL-запросов с оптимизацией.
    """
    connection.queries.clear()
    students = Student.objects.prefetch_related('teachers').all()
    list(students)
    for student in students:
        list(student.teachers.all())
    queries_count = len(connection.queries)

    context = {
        'students': students,
        'queries_count': queries_count,
        'queries': connection.queries,
        'show_analysis': True,
        'is_bad_version': False,
    }
    return render(request, 'school_app/student_list.html', context)

def student_list_bad(request):
    """
    Страница для демонстрации N+1 проблемы (БЕЗ prefetch_related).
    """
    connection.queries.clear()
    students = Student.objects.all()
    list(students)
    for student in students:
        list(student.teachers.all())
    queries_count = len(connection.queries)

    context = {
        'students': students,
        'queries_count': queries_count,
        'queries': connection.queries,
        'show_analysis': True,
        'is_bad_version': True,
    }
    return render(request, 'school_app/student_list.html', context)