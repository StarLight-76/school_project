from django.urls import path
from . import views

app_name = 'school_app'

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
]