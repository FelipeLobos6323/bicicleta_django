from django.urls import path
from . import views



urlpatterns =[

    path('',views.inicio, name=''),
    
    path('reclamos', views.reclamoss, name='reclamos')
]

