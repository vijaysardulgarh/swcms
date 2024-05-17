from django.urls import path
from . import views
from .views import timetable_view
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about.html'),
    path('staff_members',views.staff,name='staff_members.html'),
    path('student_strength',views.student_strength,name='student_strength.html'),
    path('subject_strength',views.student_strength,name='subject_strength.html'),
    path('school_subject_strength',views.student_strength,name='school_subject_strength.html'),
    path('timetable/', timetable_view, name='timetable'),
  
]
