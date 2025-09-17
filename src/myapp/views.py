from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from .models import Vehiculo
from .forms import VehiculoForm

def listar_vehiculo(request):
    vehiculo = Vehiculo.objects.all()
    return render(request,'vehiculos/lista.html',{'vehiculos':vehiculo})

def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vehiculo')  
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/crear_vehiculo.html', {'form': form}) 

