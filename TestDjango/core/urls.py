from django.urls import path
from .views import home, form_vehiculo

urlpatterns = [
    path('', home, name="home"),
    path('form-vehiculo', form_vehiculo, name="form_vehiculo"),
]