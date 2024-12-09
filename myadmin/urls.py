from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.adminhome),
    path('manageusers/', views.manageusers),
    path('manageuserstatus/', views.manageuserstatus),
    path('epadmin/', views.epadmin),
    path('cpadmin/', views.cpadmin),
    path('addcategory/', views.addcategory),
    path('addsubcategory/', views.addsubcategory)
]
