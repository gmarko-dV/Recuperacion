from django.urls import path
from . import views

urlpatterns = [
    path('',views.listar_vehiculo,name="listar_vehiculo"),
    path('crear/',views.crear_vehiculo,name="crear_vehiculo")
]
