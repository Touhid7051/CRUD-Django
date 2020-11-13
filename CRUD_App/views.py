from django.shortcuts import render

# Create your views here.
from CRUD_App.forms import Student_Admission_from


def student_admission(request):
    form = Student_Admission_from(request.POST or None)
    if form.is_valid():
        form = Student_Admission_from()
        form.save()
    context = {'form' : form}
    return render(request,'student_admission_data.html', context)