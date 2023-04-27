from django.db import models
from django.contrib.auth import get_user_model



# CREACIÓN DE MODELOS

class Categorias(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'categorias'
        verbose_name = 'Categorias'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

#CLASE PRODUCTOS

class Productos(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to= 'imgproductos/%d/%m/%Y', blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=5)
    stock = models.IntegerField(null=True, default=0)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    oferta = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

#CLASE CONTACTO

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'contacto'
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['nombre']

#CLASE CARRITO
