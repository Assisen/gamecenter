from django.contrib.auth.models import User
from django.db import models

class Tipo(models.Model):
	nombre = models.TextField(verbose_name="Nombre")
	createdat = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
	updatedat = models.DateTimeField(auto_now_add=True,verbose_name="Modificado")

	class Meta:
		verbose_name = "Tipo"
		verbose_name_plural = "Tipos"
		ordering = ["-createdat"]

	def __str__(self):
		return self.nombre

class Oferta(models.Model):
	porcentaje = models.CharField(verbose_name="Porcentaje (ejem: 10%)", max_length=4)
	porcentajeInt = models.IntegerField(verbose_name="Porcentaje (ejem: 10%)")
	createdat = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
	updatedat = models.DateTimeField(auto_now_add=True,verbose_name="Modificado")

	class Meta:
		verbose_name = "Oferta"
		verbose_name_plural = "Ofertas"
		ordering = ["-createdat"]

	def __str__(self):
		return self.porcentaje

class Producto(models.Model):
	nserie = models.CharField(verbose_name="Numero de Serie", max_length=12)
	imagen = models.ImageField(null=True, upload_to="productos", verbose_name="Foto del producto")
	nombre = models.TextField(verbose_name="Nombre")
	descripcion = models.TextField(verbose_name="Descripcion")
	existencias = models.IntegerField(verbose_name="Existencias")
	costo = models.FloatField(verbose_name="Costo")
	tipo = models.ForeignKey(Tipo, on_delete='cascade')
	marca = models.TextField(verbose_name="Marca")
	modelo = models.TextField(verbose_name="Modelo")
	oferta = models.ForeignKey(Oferta, on_delete='cascade',null=True)
	createdat = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
	updatedat = models.DateTimeField(auto_now_add=True,verbose_name="Modificado")

	class Meta:
		verbose_name = "Producto"
		verbose_name_plural = "Productos"
		ordering = ["-createdat"]

	def __str__(self):
		return self.nombre


class Favorito(models.Model):
	user = models.ForeignKey(User, on_delete='cascade')
	producto = models.ForeignKey(Producto, on_delete='cascade')
	createdat = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
	updatedat = models.DateTimeField(auto_now_add=True,verbose_name="Modificado")

	class Meta:
		verbose_name = "Favorito"
		verbose_name_plural = "Favoritos"
		ordering = ["-createdat"]


class UserProfile(models.Model):
	pp = models.ImageField(verbose_name="Foto de perfil", null=True, upload_to='profiles/',default='profiles/default/pp.png')
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Perfil"
		verbose_name_plural = "Perfiles"

class Contacto(models.Model):
	nombre = models.CharField(verbose_name="Nombre", max_length=150)
	correo = models.CharField(verbose_name="Correo", max_length=150)
	telefono = models.CharField(verbose_name="Telefono", max_length=50)
	asunto = models.CharField(verbose_name="Asunto", max_length=200)
	mensaje = models.TextField(verbose_name="Mensaje")
	createdat = models.DateTimeField(auto_now_add=True,verbose_name="Creado")

	class Meta:
		verbose_name = "Mensaje"
		verbose_name_plural = "Mensajes"
		ordering = ["-createdat"]

	def __str__(self):
		return self.nombre

class Banners(models.Model):
	banner = models.ImageField(verbose_name="Banner", null=True, upload_to='banners/')
	createdat = models.DateTimeField(auto_now_add=True,verbose_name="Creado")

	class Meta:
		verbose_name = "Banner"
		verbose_name_plural = "Banners"
		ordering = ["-createdat"]

	def __str__(self):
		return self.nombre
