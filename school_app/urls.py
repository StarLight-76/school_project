from django.urls import path
from . import views

app_name = 'school_app'

urlpatterns = [
    # Задание 1
    path('', views.student_list, name='student_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),

    # Задание 2 (анализ SQL-запросов)
    path('analysis/', views.student_list_with_analysis, name='student_list_analysis'),
    path('analysis-bad/', views.student_list_bad, name='student_list_bad'),
]