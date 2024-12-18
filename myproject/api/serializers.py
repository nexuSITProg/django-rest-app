# tutors/serializers.py

from rest_framework import serializers
from .models import Tutor, Schedule, Subject, Records

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class TutorSerializer(serializers.ModelSerializer):
    # Убираем поле schedules из основного сериализатора
    # subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Tutor
        fields = ['tutor_id', 'name', 'second_name', 'last_name', 'subject', 'experience', 'email', 'phone', 'bio']
        extra_kwargs = {
            'subject': {'read_only': True}
        }


class RecordsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Records
        fields = '__all__'