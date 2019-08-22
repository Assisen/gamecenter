from rest_framework import viewsets
from rest_framework import serializers
from .models import Producto, Oferta

class OfertaSerialiser(serializers.ModelSerializer):

	class Meta:
		model = Oferta
		fields = ('id', 'porcentaje', 'porcentajeInt')
		

class ProductoSerialiser(serializers.ModelSerializer):

	oferta = OfertaSerialiser()

	class Meta:
		model = Producto
		fields = ('id', 'imagen', 'nombre', 'descripcion', 'existencias', 'costo', 'tipo', 'marca', 'modelo', 'oferta')


class ProductoViewSet(viewsets.ModelViewSet):
	queryset = Producto.objects.all()
	serializer_class = ProductoSerialiser    


class OfertaViewSet(viewsets.ModelViewSet):
	queryset = Oferta.objects.all()
	serializer_class = OfertaSerialiser    