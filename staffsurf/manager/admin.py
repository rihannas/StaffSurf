from django.contrib import admin
from .models import Job, Person, Task, Annoucement
# Register your models here.
admin.site.register(Job)
admin.site.register(Person)
admin.site.register(Task)
admin.site.register(Annoucement)
