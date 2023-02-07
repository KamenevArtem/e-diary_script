from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
import random


def fix_marks(student_name):
	student = Schoolkid.objects.filter(full_name__contains=student_name).get()
	student_bad_marks = Mark.objects.filter(schoolkid=student, points__in=[2,3])
	for bad_mark_card in student_bad_marks:
		bad_mark_card.points = 5
		bad_mark_card.save()
	print(f"Количество плохих оценок = {student_bad_marks}")


def remove_chastisement(student_name):
	student = Schoolkid.objects.filter(full_name__contains=student_name).get()
	chastisement = Chastisement.objects.filter(schoolkid=student)
	chastisement.delete()
	print("Замечания удалены")


def create_recomendation(student_name, subject):
	student = Schoolkid.objects.filter(full_name__contains=student_name).get()
	lessons = Lesson.objects.filter(
                                 subject__title=subject,
                                 year_of_study=student.year_of_study,
                                 group_letter=student.group_letter
                                 ).order_by('-date').get()
	last_lesson = lessons.first()
	lesson_subject = last_lesson.subject
	lesson_teacher = last_lesson.teacher
	lesson_date = last_lesson.date
	praises = ['Молодец!', 'Отлично!', 'Хорошо!', 'Ты меня приятно удивил!', 
            'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!']
	Commendation.objects.create(
                             text=random.choice(praises),
                             created=lesson_date,
                             schoolkid=student,
                             subject=lesson_subject,
                             teacher=lesson_teacher
                             )
	print("Рекомендация добавлена")