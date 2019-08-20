from .models import Producto, Oferta, Tipo, Favorito, UserProfile, Contacto
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserProfileForm
from django.contrib import auth
import json


def details(request, idprod):

	producto = Producto.objects.select_related().get(id=idprod)

	tipos = Tipo.objects.all()
	return render(request, "details.html", {
		"producto":producto,
		"tipos":tipos,
	})

def register(request):

	if request.user.is_authenticated == True:
		return redirect("/")

	if request.method == 'POST':

		firstname = request.POST.get('firstName','')
		lastname = request.POST.get('lastName','')
		username = request.POST.get('username','')
		email = request.POST.get('email','')
		password = request.POST.get('password','')
		password1 = request.POST.get('password1','')

		if  password != password1:
			return redirect("/register?error=PasswordDoesntMatch")

		user = User.objects.create_user(
				username=username, 
				email=email,
				password=password,
				first_name=firstname,
				last_name=lastname
		)

		user.is_staff = True
		user.save()

		userprofile = UserProfile()
		userprofile.user = user
		userprofile.save()

		if user is not None and user.is_active:
			auth.login(request, user)
			return redirect("/")
		else:
			messages.error(request, 'Ocurrio un error')
			return redirect("/register")

	return render(request, "register.html")

def inicio(request):

	productos = Producto.objects.all()
	related   = Producto.objects.order_by('id')[:6]
	tipos = Tipo.objects.all()

	return render(
		request, "inicio.html",
		{
			"productos":productos,
			"related":related,
			"tipos":tipos,
		})

def ofertas(request):
	related = Producto.objects.order_by('?')[:5]
	tipos = Tipo.objects.all()

	ofertas = Producto.objects.all()

	return render(request, "ofertas.html",{
			"ofertas":ofertas,
			"related":related,
			"tipos":tipos,
	})

def login(request):

	if request.user.is_authenticated == False:
		if request.method == 'POST':
			username = request.POST.get('username','')
			password = request.POST.get('password','')
			user = auth.authenticate(username=username, password=password)
			
			if user is not None and user.is_active:
				auth.login(request, user)
				return redirect("/")
			else:
				messages.error(request, 'Las credenciales son incorrectas')
				return redirect("/login")
		return render(request, "login.html")
	else:
		return redirect("/")


def logout(request):
	if request.user.is_authenticated == False:
		return redirect("/")

	auth.logout(request)
	return redirect("/")

def categoria(request, idcat=0):
	productos = Producto.objects.all().filter(tipo=idcat)
	tipos = Tipo.objects.all()
	return render(request, "inicio.html", {
		"productos":productos,
		"tipos":tipos,
	})

def search(request):
	q = request.GET.get("q",'')
	productos = Producto.objects.all().filter(descripcion__contains=q)
	tipos = Tipo.objects.all()
	return render(request, "search.html", {
		"productos":productos,
		"tipos":tipos,
	})

def favorite(request, idprod):
	if request.user.is_authenticated == True:
		
		producto = Producto.objects.get(id=idprod)
		
		try:
			favorite_exists = Favorito.objects.get(producto=producto,user=request.user)
		except Exception as e:
			favorite_exists = None
			
		response_data = {}
		
		if favorite_exists is None:
			favorito = Favorito()
			favorito.user = request.user
			favorito.producto = producto
			favorito.save()
			response_data['result'] = 'success'
			response_data['message'] = 'Agregado a tu lista'
		else:
			response_data['result'] = 'success'
			response_data['message'] = 'Ya existe en tu lista'

		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:

		response_data = {}
		response_data['result'] = 'error'
		response_data['message'] = 'Debes iniciar sesion para hacer esta accion'
		
		return HttpResponse(json.dumps(response_data), content_type="application/json")

def delete_favorite(request, idprod):
	if request.user.is_authenticated == True:
		
		producto = Producto.objects.get(id=idprod)
		
		try:
			favorite_exists = Favorito.objects.get(producto=producto,user=request.user)
		except Exception as e:
			favorite_exists = None
			
		response_data = {}
		
		if favorite_exists is None:
			response_data['result'] = 'error'
			response_data['message'] = 'Ya no existe en tu lista'
		else:
			favorite_exists.delete()
			response_data['result'] = 'success'
			response_data['message'] = 'Eliminado de tu lista'

		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:

		response_data = {}
		response_data['result'] = 'error'
		response_data['message'] = 'Debes iniciar sesion para hacer esta accion'
		
		return HttpResponse(json.dumps(response_data), content_type="application/json")

def pfavs(request):
	tipos = Tipo.objects.all()
	productos = None

	if request.user.is_authenticated == True:

		try:
			productos = Favorito.objects.all().filter(user=request.user)
		except Exception as e:
			productos = None

		return render(request, "pfavs.html", {
			"productos":productos,
			"tipos":tipos,
		})

	else:
		return redirect("/")

def profile(request):
	if request.user.is_authenticated == False:
		return redirect("/")

	tipos = Tipo.objects.all()

	if request.method == 'POST':

		if request.POST.get('frm','') == 'frm_pp':

			userp = UserProfile.objects.get(user=request.user)
			userp.pp = request.FILES.get('pp',None)
			userp.save()

			messages.success(request, 'Tu foto de perfil se actualizo correctamente')

		elif request.POST.get('frm','') == 'frm_txt':

			user = User.objects.get(id=request.user.id)
			user.username = request.POST.get('username','')
			user.first_name = request.POST.get('firstName','')
			user.last_name = request.POST.get('lastName','')
			user.email = request.POST.get('email','')
			user.save()

			messages.success(request, 'Tu datos se actualizaron correctamente')

		elif request.POST.get('frm','') == 'frm_pass':
			if request.POST.get('pass1','') == request.POST.get('pass2',''):

				user = User.objects.get(id=request.user.id)
				
				if user.check_password(request.POST.get('pass','')):

					user.set_password(request.POST.get('pass1',''))
					user.save()

					update_session_auth_hash(request, user)

					messages.success(request, 'Tu contraseña se actualizo correctamente')
				else:
					messages.error(request, 'Tu contraseña es incorrecta')
			else:
				messages.error(request, 'Las contraseñas nuevas no coinciden')
		else:
			messages.error(request, 'Accion invalida')

		return redirect("/profile")
	
	return render(request, "profile.html", {
		"tipos":tipos,
	})

def contacto(request):

	if request.method=='POST':

		contacto = Contacto()

		contacto.nombre = request.POST.get('name','')
		contacto.correo = request.POST.get('email','')
		contacto.telefono = request.POST.get('tel','')
		contacto.asunto = request.POST.get('asunto','')
		contacto.mensaje = request.POST.get('message','')

		contacto.save()

		messages.success(request, 'Mensaje enviado, en breve nos comunicaremos con usted')
		return redirect("/contacto")


	tipos = Tipo.objects.all()
	return render(request, "contacto.html", {
		"tipos":tipos,
	})	

def handler404(request, exception):
    return render(request, 'error/404.html')


def handler500(request):
    return render(request, 'error/500.html')