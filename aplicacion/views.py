from .models import Producto
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

def lista_productos(request):
    productos = Producto.objects.all()
    
    # #Pginacion
    page = request.GET.get('page',1)
    paginator = Paginator(productos, 15)  # cantidad de productos por página
    page_obj = paginator.get_page(page)
  
    return render(request, 'lista_productos.html', {'productos': page_obj})

def inicio(request):
    return render(request, 'inicio.html')

def productos(request):
    return render(request, 'productos.html')

def detalle(request, producto_id):
    # Recupera el producto específico por su ID
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'detalle.html', {'producto': producto})

#Email

def contacto(request):
    return render(request, 'contacto.html')

def contact(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        email = request.POST['email']
        asunto = request.POST['asunto']
        mensaje = request.POST['mensaje']
        espacio = request.POST['espacio']

        template = render_to_string('email_contacto.html', {
          'nombre': 'Nombre: ' + nombre,
          'email' : 'Email: ' + email,
          'mensaje': 'Mensaje: ' + mensaje,
          'espacio': espacio,
        })

        email = EmailMessage(
            asunto,
            template,
            settings.EMAIL_HOST_USER,
            ['comercializadorabvspaeme@gmail.com']
        )

        email.fail_silently = False
        email.send()

        messages.success(request, 'Enviado correctamente.')
        return redirect('contacto')