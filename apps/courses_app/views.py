from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):

    context = {
    "courses" : Course.objects.all()
    }
    return render(request, "courses_app/index.html", context)

def courses(request):
    # insert into Course (Course_Name, Description) values (Course_Name, Description, now(), now() )
    Course.objects.create(course=request.POST['course'], description= request.POST['description'])
    return redirect('/')

def remove(request, id):
    # from course grab id
    erase = Course.objects.get(id=id)
    # if request.method == "GET"
    if request.method == "GET":
        return render(request, 'courses_app/index2.html', {"course" : erase})
    erase.delete()
    return redirect('/')
