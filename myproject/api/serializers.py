# tutors/serializers.py

from rest_framework import serializers
from .models import Tutor, Schedule, Subject

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['day_of_week', 'start_time', 'end_time']  # Включаем поле subject_name

class TutorSerializer(serializers.ModelSerializer):
    schedule = serializers.SerializerMethodField()
    subject_name = serializers.CharField(source='subject.subject_name', read_only=True)  # Добавляем название предмета
    
    class Meta:
        model = Tutor
        fields = ['name', 'second_name', 'last_name', 'experience', 'schedule', 'subject_name', 'phone']

    def get_schedule(self, tutor):
        schedule = Schedule.objects.filter(tutor=tutor)
        return ScheduleSerializer(schedule, many=True).data