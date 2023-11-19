from django.db import models
import locale

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='img_productos', null=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
   
    def precio_con_separador_de_miles(self):
        locale.setlocale(locale.LC_ALL, '')  # Configura la localización del sistema

        # Formatea el precio con separador de miles
        return locale.format_string("%.0f", self.precio, grouping=True)

    def __str__(self):
        return self.nombre
    
