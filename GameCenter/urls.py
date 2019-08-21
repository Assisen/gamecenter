from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls import url
from inicio import views
from django.views.static import serve

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
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += [
        url(r'^uploads/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
        url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    ]


handler404 = 'inicio.views.handler404'
handler500 = 'inicio.views.handler500'

# Change admin site title
admin.site.site_header = "GameCenter"
admin.site.site_title = "Administracion"
admin.site.index_title = "Administracion"