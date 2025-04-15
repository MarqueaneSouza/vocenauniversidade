from django.urls import path

from . import views

urlpatterns = [
    path('painel/', views.painel_acompanhamento, name='painel_acompanhamento'),
]