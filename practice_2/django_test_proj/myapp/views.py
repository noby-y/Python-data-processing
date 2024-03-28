from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import Student
import random

# Create your views here.


# def hello(request):
#    text = """<h1>welcome to my app !</h1>"""
#    return HttpResponse(text)

def hello(request):
    return render(request, "hello.html", {})

def crudops(request):
    #Creating an entry
    
    new_name = f"test{random.randint(1,10000)}"
    
    new_student = Student(
        name = new_name, surname = "Kuruch", 
        phonenumber = "002376970"
    )
    new_student.save()
    
    #Read ALL entries
    objects = Student.objects.all()
    res ='Printing all Student entries in the DB : <br>'
    
    for elt in objects:
        res += elt.name+"<br>"
    
    #Read a specific entry:
    # student_test = Student.objects.get(name = new_name)
    # res += 'Printing One entry <br>'
    # res += student_test.name
    
    # #Delete an entry
    # res += '<br> Deleting an entry <br>'
    # student_test.delete()
    
    # #Update
    # new_student = Student(
    #     name = "Tigran", surname = "Avanesov", 
    #     phonenumber = "009999999"
    # )
    
    # new_student.save()
    # res += 'Updating entry<br>'
    
    # new_student = Student.objects.get(name = 'sorex')
    # new_student.name = 'Whatever'
    # new_student.save()
    
    return HttpResponse(res)