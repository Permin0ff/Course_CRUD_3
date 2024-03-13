from django.forms import ModelForm, CharField, IntegerField
from .models import Person

class PersonForm(ModelForm):
    name = CharField(label='Введите имя')
    age = IntegerField(label='Введите возраст')
    class Meta:
        model = Person
        fields = ['name', 'age']
