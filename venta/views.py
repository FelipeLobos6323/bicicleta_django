from django.shortcuts import render

# Create your views here.

def inicio(request):
    
    return render(request, 'venta/index.html')
 


def reclamoss(request):
    return render(request, 'venta/reclamoss.html')