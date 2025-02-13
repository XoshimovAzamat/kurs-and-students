
from django.contrib import admin
from django.urls import path, include
from configapp.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('configapp.urls'))
]
