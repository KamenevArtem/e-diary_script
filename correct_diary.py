from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import random


PRAISES = ['Молодец!', 'Отлично!', 'Хорошо!', 'Ты меня приятно удивил!',
           'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!']

def get_student_card(student_name):
    try:
        student = Schoolkid.objects.filter(full_name__contains=student_name).get()
        return student
    except Schoolkid.DoesNotExist:
        raise Schoolkid.DoesNotExist("Введенное Вами имя не существует")
    except Schoolkid.MultipleObjectsReturned:
        raise Schoolkid.MultipleObjectsReturned("Введеное имя имеет несколько совпадений")


def fix_marks(student_name):
    student = get_student_card(student_name)
    changed_marks = Mark.objects.filter(schoolkid=student, points__in=[2,3]).update(points=5)
    print(f"Было исправлений: {changed_marks}")


def remove_chastisement(student_name):
	student = get_student_card(student_name)
	chastisement = Chastisement.objects.filter(schoolkid=student)
	chastisement.delete()
	print("Замечания удалены")


def create_recomendation(student_name, subject):
    student = get_student_card(student_name)
    lessons = Lesson.objects.filter(
                                    subject__title=subject,
                                    year_of_study=student.year_of_study,
                                    group_letter=student.group_letter
                                    ).order_by('-date')
    if len(lessons) == 0:
        print("Введеный Вами урок не существует")
    else:
        last_lesson = lessons.first()
        lesson_subject = last_lesson.subject
        lesson_teacher = last_lesson.teacher
        lesson_date = last_lesson.date
        Commendation.objects.create(
                                    text=random.choice(PRAISES),
                                    created=lesson_date,
                                    schoolkid=student,
                                    subject=lesson_subject,
                                    teacher=lesson_teacher
                                    )
        print("Рекомендация добавлена")