from django.db import models

class Teacher(models.Model):
    name = models.CharField('Имя', max_length=100)
    subject = models.CharField('Предмет', max_length=100)

    def __str__(self):
        return f"{self.name} ({self.subject})"

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Student(models.Model):
    name = models.CharField('Имя', max_length=100)
    age = models.IntegerField('Возраст')
    grade = models.CharField('Класс', max_length=10)

    # ЗАДАНИЕ 1: меняем ForeignKey на ManyToManyField
    teachers = models.ManyToManyField(
        Teacher,
        verbose_name='Учителя',
        related_name='students',   # для обратной связи
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'