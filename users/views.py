from django.shortcuts import render, redirect
from .models import Persona
from .form import PersonaForm

# Create your views here.
def registrar(request):
    if request.method == 'POST':
        form =PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    form = PersonaForm()
    return render (request,'registrarUsuario.html',{'form':form})

def listar(request):
    personas = Persona.objects.all()
    return render(request,'listarUsuario.html',{'personas':personas})


