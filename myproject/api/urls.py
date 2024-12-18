from django.urls import path
from .views import (
    TutorListCreateView,
    TutorDetailView,
    ScheduleListCreateView,
    ScheduleDetailView,
    SubjectListCreateView,
    SubjectDetailView,
    RecordsListCreateView, 
    RecordsDetailView        
)

urlpatterns = [
    path('api/tutors/', TutorListCreateView.as_view(), name='tutor-list-create'),
    path('api/tutors/<int:pk>/', TutorDetailView.as_view(), name='tutor-detail'),
    path('api/schedules/', ScheduleListCreateView.as_view(), name='schedule-list-create'),
    path('api/schedules/<int:pk>/', ScheduleDetailView.as_view(), name='schedule-detail'),
    path('api/subjects/', SubjectListCreateView.as_view(), name='subject-list-create'),
    path('api/subjects/<str:pk>/', SubjectDetailView.as_view(), name='subject-detail'),
    path('api/records/', RecordsListCreateView.as_view(), name='records-list-create'), 
    path('api/records/<int:pk>/', RecordsDetailView.as_view(), name='records-detail') 
]