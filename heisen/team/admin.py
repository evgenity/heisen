from django.contrib import admin

# Register your models here.
from .models import Person, Tag

admin.site.register(Person)
admin.site.register(Tag)
