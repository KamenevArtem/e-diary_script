# e-diary_script

Скрип предназначен для внесения изменений в электронный дневник учеников, а именно на изменение плохих оценок, удаление замечаний учителей и внесение похвал от учителей по любому интересующему предмету.

## Как установить

Для работы скрипта Python3 должен быть установлен, необходимо произвести следующую последовательность действий:

* скачайте скрип по [ссылке](https://github.com/KamenevArtem/e-diary_script);
* файл `correct_diary.py` поместите в головную дирректорию электронного дневника рядом с файлом `manage.py`;

## Как запустить

* откройте командную строку;
* при помощи команды `cd "полный путь к директории"` перейдите в головную директорию электронного дневника;
* введите команду `python manage.py shell`;
* скопируйте и вставьте следующий блок команд:
```python
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
from correct_diary import fix_marks
from correct_diary import remove_chastisement
from correct_diary import create_recomendation
from correct_diary import praises
import random
```
* в зависимости от того, что необходимо сделать, вызовите нужную функцию.

## Как использовать

Скрипт состоит из трёх функций, выполняющих различные задачи:

### fix_marks

Находит все плохие оценки заданного ученика и исправляет их на пятерки. Для её вызова необходимо ввести команду:

```python
fix_marks("Фамилия и имя необходимого ученика")
```

### remove_chastisement

Удаляет все имеющиеся у конкретного ученика замечания от учителей. Для ёё вызова необходимо ввести команду:

```python
remove_chastisement("Фамилия и имя необходимого ученика")
```

### create_recomendation

Данная функция может внести в электронный дневник ученика похвалу по интересующему предмету за последний урок. Вызвать её можно командой:

```python
create_recomendation("Фамилия и имя необходимого ученика", "Интересующий предмет", praises)
```

Набор похвал хранится в переменной praises. Если пользователь хочет изменить этот набор, то в эту переменную можно перезаписать в shell, введя следующую команду:
```
praises=["Слова похвалы",]
```

P.S. Все аргументы функций необходимо вводить в ковычках.

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [devman](https://devman.org/)