# school_app/migrations/0002_auto_20250101_0000.py
from django.db import migrations, models


def migrate_teacher_to_teachers(apps, schema_editor):
    Student = apps.get_model('school_app', 'Student')

    for student in Student.objects.all():
        # Переносим данные из старого поля teacher в новое teachers
        if student.teacher:  # У студента есть учитель
            student.teachers.add(student.teacher)


class Migration(migrations.Migration):
    dependencies = [
        ('school_app', '0001_initial'),  # Название первой миграции
    ]

    operations = [
        # 1. Добавляем новое поле ManyToMany
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(
                related_name='students',
                to='school_app.teacher',
                verbose_name='Учителя',
                blank=True
            ),
        ),

        # 2. Переносим данные из ForeignKey в ManyToMany
        migrations.RunPython(migrate_teacher_to_teachers),

        # 3. Удаляем старое поле teacher (ForeignKey)
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
    ]