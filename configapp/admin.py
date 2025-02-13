from sys import modules

from django.contrib import admin
from .models import *

class studentAdmin(admin.ModelAdmin):
    list_display = ('kurs_id','full_name', 'phone_number', 'email')
    list_display_links = ['full_name']
    search_fields = ['full_name', 'kurs_id']
    list_editable = ['phone_number']

class kursAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_time', 'finish_time')
    list_display_links = ['title']
    search_fields = ['title']


admin.site.register(Student, studentAdmin)
admin.site.register(Kurs, kursAdmin)
