from django.contrib import admin
from myapp.models import Person
# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = ['firstname' , 'lastname' , 'age' , 'date' ]

admin.site.register(Person,Admin)