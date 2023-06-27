from django.shortcuts import render
from .models import Cliente,Genero
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
#--------------------------- VISTAS DE INDEX ---------------------------------------
def inicio(request):
    
    return render(request, 'venta/index.html')

@login_required(login_url='/accounts/login/')
def clienteindex(request):
    request.session["usuario"]="felipe"
    lista_clientes = Cliente.objects.all() #select * from Alumno
    usuario = request.session["usuario"]
    context = {"clientes":lista_clientes, "usu": usuario}
    return render(request,'venta/clienteindex.html', context)


def reclamoss(request):
    return render(request, 'venta/reclamoss.html')

def carrito(request):
    return render(request, 'venta/carrito.html')

def cascoss(request):
    return render(request, 'venta/cascoss.html')  

def bicicletass(request):
    return render(request, 'venta/bicicletass.html')  

def login(request):
    return render(request, 'venta/login.html') 

def repuesto(request):
    return render(request, 'venta/repuesto.html') 

def nosotros(request):
    return render(request, 'venta/nosotros.html') 

def json(request):
    return render(request, 'venta/json.html') 

# ----------------------------- ESTA PARTE ES NUEVA -----------------------------



def lista_clientes(request):
    lista_clientes = Cliente.objects.raw('select * from venta_cliente') #select * from Cliente
    context = {"clientes":lista_clientes}
    return render(request,'venta/clienteindex.html', context)
    
def lista_genero(request):
    lista_generos = Genero.objects.all() #select * from Genero
    context = {"generos":lista_generos}
    return render(request,'venta/otro.html', context)

def agregar_clientes(request):
    if request.method != "POST":
        lista_generos = Genero.objects.all()
        context = {"generos":lista_generos}
        return render(request,'venta/clientes_add.html', context)
    else:
        #izq: variable local - der: input del formulario (name)
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apePaterno = request.POST["apePat"]
        apeMaterno = request.POST["apeMat"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"] #id_genero (value)
        telefono = request.POST["telefono"]
        mail = request.POST["email"]
        direccion = request.POST["direccion"]

        objGenero = Genero.objects.get(id_genero = genero)
        #se crea onjeto alumno, izq: campo del model - der: variable local
        objCliente = Cliente.objects.create(
            rut              = rut,
            nombre           = nombre,
            apellido_paterno = apePaterno,
            apellido_materno = apeMaterno,
            fecha_nacimiento = fechaNac,
            id_genero        = objGenero,
            telefono         = telefono,
            email            = mail,
            direccion        = direccion,
            activo           = 1)
        
        objCliente.save() #insert 
        lista_generos = Genero.objects.all()
        context = {"mensaje":"Se guardó Cliente", "generos":lista_generos}
        return render(request,'venta/clientes_add.html', context)
    
    

#------------------------------------------------------------PROFESORA----------------------------------------------------------------------------------------

def eliminar_cliente(request,pk):
    try:
        cliente = Cliente.objects.get(rut=pk)
        cliente.delete()
        mensaje = "El cliente se eliminó"
        lista_clientes = Cliente.objects.all()
        context = {"clientes":lista_clientes, "mensaje":mensaje}
        return render(request,'venta/clienteindex.html', context)
    except:
        mensaje = "El cliente NO se eliminó"
        lista_clientes = Cliente.objects.all()
        context = {"clientes":lista_clientes, "mensaje":mensaje}
        return render(request,'venta/clienteindex.html', context)

def buscar_cliente(request,pk):
    if pk != "":
        cliente = Cliente.objects.get(rut=pk)
        lista_generos = Genero.objects.all() 
        context = {"cliente":cliente, "generos":lista_generos}
        return render(request,'venta/clientes_edit.html', context)
    else:
        mensaje = "El cliente NO existe"
        context = {"mensaje":mensaje}
        return render(request,'venta/clienteindex.html', context)

def modificar_cliente(request):
    if request.method == "POST":
        #izq: variable local - der: input del formulario (name)
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apePaterno = request.POST["apePat"]
        apeMaterno = request.POST["apeMat"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"] #id_genero (value)
        telefono = request.POST["telefono"]
        mail = request.POST["mail"]
        direccion = request.POST["direccion"]

        objGenero = Genero.objects.get(id_genero = genero)
        #se crea onjeto alumno, izq: campo del model - der: variable local
        objCliente = Cliente()
        objCliente.rut              = rut
        objCliente.nombre           = nombre
        objCliente.apellido_paterno = apePaterno
        objCliente.apellido_materno = apeMaterno
        objCliente.fecha_nacimiento = fechaNac
        objCliente.id_genero        = objGenero
        objCliente.telefono         = telefono
        objCliente.email            = mail
        objCliente.direccion        = direccion
        objCliente.activo           = 1
        
        objCliente.save() #update 
        lista_generos = Genero.objects.all()
        context = {"mensaje":"Se actualizó cliente", "generos":lista_generos, "cliente":objCliente}
        return render(request,'venta/clientes_edit.html', context)
    else:
        lista_clientes = Cliente.objects.all()
        context = {"clientes":lista_clientes}
        return render(request,'venta/clienteindex.html', context)

def home(request):
    context = {}
    return render(request,'venta/home.html', context)

#------------------------------------------------------------------------------------------------------------

