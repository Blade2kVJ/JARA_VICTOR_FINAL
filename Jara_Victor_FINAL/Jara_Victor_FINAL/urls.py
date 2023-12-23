"""
URL configuration for Jara_Victor_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from seminario_app.views import ParticipanteListView, ParticipanteDetailView, ParticipanteCreateView, institucion_list, institucion_create, Usuario
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('participantes/', ParticipanteListView.as_view(), name='participante-list'),
    path('participantes/<int:pk>/', ParticipanteDetailView.as_view(), name='participante-detail'),
    path('participantes/crear/', ParticipanteCreateView.as_view(), name='participante-create'),
    path('instituciones/', institucion_list, name='institucion-list'),
    path('instituciones/crear/', institucion_create, name='institucion-create'),
    path('usuario', Usuario),
]