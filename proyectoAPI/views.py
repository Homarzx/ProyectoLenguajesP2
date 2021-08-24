from django.shortcuts import render
from .forms import PersonaForm
# Create your views here.

def ingreso(request):
	data={
		'form':PersonaForm()
	}
	if request.method =='POST':
		formulario=PersonaForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
		else:
			data["form"]=formulario
	return render(request,'proyectoAPI/ingreso.html',data)
