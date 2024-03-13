from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Person
from .forms import PersonForm


# Получение данных из БД
def index(request):
    form = PersonForm()
    people = Person.objects.all()
    return render(request, 'index.html', {'form': form, 'people': people})


# Сохранение данных в БД
def create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/')


# Изменение данных в БД
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == 'POST':
            form = PersonForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/')
        else:
            form = PersonForm(instance=person)
            return render(request, 'edit.html', {'form': form})
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')


# Удаление данных из БД
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
