from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import random


praises = ['Молодец!', 'Отлично!', 'Хорошо!', 'Ты меня приятно удивил!',
           'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!']

def fix_marks(student_name):
    try:
        student = Schoolkid.objects.filter(full_name__contains=student_name).get()
        changed_marks = Mark.objects.filter(schoolkid=student, points__in=[2,3]).update(points=5)
        print(f"Было исправлено {changed_marks} оценок")
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist("Введенное Вами имя не существует")
    except MultipleObjectsReturned:
        raise MultipleObjectsReturned("Введеное имя имеет несколько совпадений")


def remove_chastisement(student_name):
	student = Schoolkid.objects.filter(full_name__contains=student_name).get()
	chastisement = Chastisement.objects.filter(schoolkid=student)
	chastisement.delete()
	print("Замечания удалены")


def create_recomendation(student_name, subject, praises):
    try:
        student = Schoolkid.objects.filter(full_name__contains=student_name).get()
        lessons = Lesson.objects.filter(
                                        subject__title=subject,
                                        year_of_study=student.year_of_study,
                                        group_letter=student.group_letter
                                        ).order_by('-date')
        last_lesson = lessons.first()
        lesson_subject = last_lesson.subject
        lesson_teacher = last_lesson.teacher
        lesson_date = last_lesson.date
        Commendation.objects.create(
                                text=random.choice(praises),
                                created=lesson_date,
                                schoolkid=student,
                                subject=lesson_subject,
                                teacher=lesson_teacher
                                )
        print("Рекомендация добавлена")
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist("Введенное Вами имя или предмет не найдено")
    except AttributeError:
        raise AttributeError("Введеный Вами предмет не найден")
    except MultipleObjectsReturned:
        raise MultipleObjectsReturned("Введеное имя имеет несколько совпадений")