# Этот файл генерируется автоматически при первой миграции.

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('subject', models.CharField(max_length=100, verbose_name='Предмет')),
            ],
            options={'verbose_name': 'Учитель', 'verbose_name_plural': 'Учителя'},
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('grade', models.CharField(max_length=10, verbose_name='Класс')),
                ('teacher', models.ForeignKey(
                    blank=True, null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='students_old',
                    to='school_app.teacher',
                    verbose_name='Учитель'
                )),
            ],
            options={'verbose_name': 'Ученик', 'verbose_name_plural': 'Ученики'},
        ),
    ]