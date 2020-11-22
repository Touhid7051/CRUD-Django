from django.urls import path
from .views import student_admission,index,student_list
urlpatterns = [
    path('', index ,name='index'),
    path('admission_form/', student_admission ,name='student_admission'),
    path('student_list/', student_list ,name='student_list'),
]