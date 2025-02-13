
from django.contrib import admin
from django.urls import path, include
from configapp.views import student_index, kurs_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1/', student_index),
    path('index2/', kurs_index),
]
