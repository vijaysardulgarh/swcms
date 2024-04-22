from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about.html'),
    path('staff_members',views.staff,name='staff_members.html'),
    path('student_strength',views.student_strength,name='student_strength.html'),
]
