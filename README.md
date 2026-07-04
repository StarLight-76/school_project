# Школьный проект Django

## Задания

### Задание 1
- Заменить ForeignKey на ManyToManyField между Student и Teacher.
- Добавить related_name='students'.
- Создать миграцию с переносом данных.
- Исправить шаблон student_list.html – выводить всех учителей вложенным циклом.

### Задание 2 
- Установить django-debug-toolbar.
- Проанализировать SQL-запросы.
- Устранить N+1 проблему с помощью prefetch_related.
- Предоставить доказательства (страницы /analysis/ и /analysis-bad/).

## Результаты оптимизации

| Версия | Количество SQL-запросов |
|--------|--------------------------|
| Без prefetch_related | N + 1 (для каждого студента отдельный запрос) |
| С prefetch_related   | 2 (всего два запроса) |

## Запуск

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata school.json   # загружаем тестовые данные
python manage.py createsuperuser
python manage.py runserver