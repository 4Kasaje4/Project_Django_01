from django.shortcuts import render , redirect
from django.http.response import HttpResponse
from myapp.models import Person
from django.contrib import messages
# Create your views here.

def index(request) :
    n = 0
    person = Person.objects.all()
    for i in person :
        n = n + 1

    return render(request,'index.html',{'person' : person, 'num' : n} )

def about(request):
    return render(request,'about.html')

def form(request):
    if request.method == "POST":
        # input data
        firstname = request.POST['firstname']
        lastname = request.POST['Lastname']
        age = request.POST['age']

        person = Person.objects.create(
            firstname = firstname,
            lastname = lastname,
            age = age
        )
        person.save()
        messages.success(request,"Successfully")
        return redirect('/')
    else:
        return render(request , 'form.html')

def edit(request,person_id):

    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['Lastname']
        age = request.POST['age']
        person = Person.objects.get(id=person_id)
        person.firstname = firstname
        person.lastname = lastname
        person.age = age
        person.save()
        messages.success(request,"Edit Successfully")
        return redirect('/')
    else :    
        person_id = Person.objects.get(id=person_id)
        return render(request,'edit.html', {'person_id': person_id})
    

def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request,"Delete Successfully")
    return redirect('/')
