from django.urls import path
from proyectoAPI import views


urlpatterns = [
    path('', views, name="ingreso"),
]
