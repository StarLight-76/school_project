from django.contrib import admin
from .models import Teacher, Student

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    search_fields = ('name', 'subject')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'grade', 'get_teachers')
    filter_horizontal = ('teachers',)   # удобный виджет для ManyToMany

    def get_teachers(self, obj):
        return ", ".join([t.name for t in obj.teachers.all()])
    get_teachers.short_description = 'Учителя'