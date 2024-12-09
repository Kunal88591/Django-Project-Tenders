from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('service/', views.service),
    path('register/', views.register),
    path('login/', views.login),
    path('verify/', views.verify),
    path('user/',include('user.urls')),
    path('myadmin/',include('myadmin.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


