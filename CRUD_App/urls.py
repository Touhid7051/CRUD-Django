from django.urls import path
from .views import student_admission
urlpatterns = [
    path('admission_form/', student_admission ,name='student_admission')
]