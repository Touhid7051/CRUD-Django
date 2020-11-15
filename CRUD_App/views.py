from django.shortcuts import render,redirect

# Create your views here.
from CRUD_App.forms import Student_Admission_from



def index(request):
    return render(request,'index.html')

def student_admission(request):
    form = Student_Admission_from(request.POST , request.FILES)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('index')
    context = {'form' : form}
    return render(request,'student_admission_data.html', context)