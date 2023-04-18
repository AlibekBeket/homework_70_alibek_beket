# homework_70_alibek_beket
### Детальный просмотр проекта или задачи через api
Путь url = api/issue_detail/<int:pk> (задача) или api/project_detail/<int:pk> (проект)

pk - это ключ объекта

Метод GET

Возвращает словарь одного объекта
```
Примерно как должно выглядеть
{
  "field_1": "value_1",
  "field_2": "value_2",
  ...
  "field_n": "value_n",
}
(в value может быть список из нескольких значений)
```
### Обновление всех полей проекта или задачи через api
Путь url = api/issue_update/<int:pk> (задача) или api/project_update/<int:pk> (проект)

pk - это ключ объекта

Метод PUT

Нужно написать в body словарь со всеми полями объекта
```
проект
{
    "id": int,
    "name": "str",
    "description": "str",
    "start_date": "date",
    "end_date": "date",
    "is_deleted": bool,
    "user": [int]
}
задача
{
    "id": int,
    "summary": "str",
    "description": "str",
    "status": int,
    "created_at": "datetime",
    "updated_at": "datetime",
    "type": [int],
    "project": int
}
(указал какие должны значения полей:
[int] - список из числовых значений, str - строка, int - числовое значение, date - дата без времени, datetime - дата с временем)
```
Возвращает словарь обновленного объекта
```
{
  "field_1": "value_1",
  "field_2": "value_2",
  ...
  "field_n": "value_n",
}
(в value может быть список из нескольких значений)
```
### Удаление проекта или задачи через api
Путь url = api/issue_delete/<int:pk> (задача) или api/project_delete/<int:pk> (проект)

pk - это ключ объекта

Метод DELETE

Возвращает:
```
Задача
{'delete project pk': int}
Проект
{'delete project pk': int}
Значения поля int - числовое занчение(в данном случае ключ задачи или проекта)
```
