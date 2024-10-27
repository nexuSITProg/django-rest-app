# tutors/views.py

from django.http import JsonResponse
from .models import Tutor, Schedule

def tutor_schedule(request):
    # Получаем всех репетиторов
    tutors = Tutor.objects.all().select_related('subject')
    response_data = []

    for tutor in tutors:
        # Получаем расписание для каждого репетитора, используя его идентификатор
        tutor_schedules = Schedule.objects.filter(tutor_id=tutor.tutor_id)

        schedule_list = [
            {
                'day': schedule.day_of_week,
                'time': f'{schedule.start_time.strftime("%H:%M")}-{schedule.end_time.strftime("%H:%M")}',
            } for schedule in tutor_schedules
        ]

        tutor_data = {
            'name': tutor.name,
            'surname': tutor.last_name,
            'experience': tutor.experience,
            'schedule': schedule_list,
            'phone': tutor.phone,
            'bio': tutor.bio,
            'subject': tutor.subject.subject_name if tutor.subject else None  # Добавляем предмет, если он есть
        }
        response_data.append(tutor_data)

    return JsonResponse(response_data, safe=False)