from django.urls import path
from .views import home, form_vehiculo, form_mod_vehiculo

urlpatterns = [
    path('', home, name="home"),
    path('form-vehiculo', form_vehiculo, name="form_vehiculo"),
    path('form-mod-vehiculo/<id>', form_mod_vehiculo, name="form_mod_vehiculo"),
]