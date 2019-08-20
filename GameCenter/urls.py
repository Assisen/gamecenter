from django.conf import settings
from django.contrib import admin
from django.urls import path
from inicio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
    
    path('details/<int:idprod>', views.details, name="details"),
    path('ofertas', views.ofertas, name="ofertas"),
    path('categoria/<int:idcat>', views.categoria, name="categoria"),
    path('search', views.search, name="search"),

    path('favorite/<int:idprod>', views.favorite, name="favorite"),
    path('delete/fav/<int:idprod>', views.delete_favorite, name="delete_favorite"),
    path('profile/favs', views.pfavs, name="pfavs"),
    path('profile', views.profile, name="profile"),

    path('contacto', views.contacto, name="contacto"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]

handler404 = 'inicio.views.handler404'
handler500 = 'inicio.views.handler500'

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)