from django.db import migrations, models

def migrate_teacher_to_teachers(apps, schema_editor):
    Student = apps.get_model('school_app', 'Student')
    for student in Student.objects.all():
        if student.teacher:
            student.teachers.add(student.teacher)

class Migration(migrations.Migration):
    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
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
        migrations.RunPython(migrate_teacher_to_teachers),
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
    ]