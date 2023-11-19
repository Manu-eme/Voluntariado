# urls.py
from django.urls import path
from . import views
from .views import contact

urlpatterns = [
   
    path('', views.inicio, name='inicio'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('detalle/<int:producto_id>/', views.detalle, name='detalle'),
    path('contact/', contact, name='contact'),
    
]

