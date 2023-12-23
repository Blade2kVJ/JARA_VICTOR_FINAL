from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Participante, Institucion
from .forms import ParticipanteForm ,InstitucionForm

# Create your views here.

class ParticipanteListView(ListView):
    model = Participante
    template_name = 'participante_list.html'
    context_object_name = 'Participantes'

class ParticipanteDetailView(DetailView):
    model = Participante
    template_name = 'participante_detail.html'

class ParticipanteCreateView(CreateView):
    model = Participante
    template_name = 'participante_form.html'
    form_class = ParticipanteForm
    success_url = '/participantes/'

def institucion_list(request):
    instituciones = Institucion.objects.all()
    return render(request, 'institucion_list.html', {'instituciones': instituciones})

def institucion_create(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('institucion-list')
    else:
        form = InstitucionForm()
    return render(request, 'institucion_form.html', {'form': form})

@api_view(['GET'])
def Usuario(request):
    datos_autor = {
        'username': "Victor Jara",
        'Seccion': "IEI-171-N4",
    }
    return Response(datos_autor)