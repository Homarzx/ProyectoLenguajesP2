from django.urls import path
from .views import ingreso


urlpatterns = [
    path('', ingreso, name="ingreso"),
]
