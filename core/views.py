from django.shortcuts import render, redirect
from .models import Person

def home(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})

def save(request):
    newName = request.POST.get("name")
    Person.objects.create(name=newName)
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})

def edit(request, id):
    person = Person.objects.get(id=id)
    return render(request, "update.html", {"person": person})

def update(request, id):
    editName = request.POST.get("name")
    person = Person.objects.get(id=id)
    person.name = editName
    person.save()
    return redirect(home)

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect(home)