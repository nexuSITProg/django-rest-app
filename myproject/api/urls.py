# tutors/urls.py

from django.urls import path
from .views import tutor_schedule

urlpatterns = [
    path('api/tutors/', tutor_schedule, name='tutor_schedule'),
]