from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.userhome),
    path('viewcategory/', views.viewcategory),
    path('viewsubcategory/', views.viewsubcategory),
    path('addtender/', views.addtender),
    path('viewtender/', views.viewtender),
    path('tendermain/', views.tendermain),
    path('funds/', views.funds),
    path('cancel/', views.cancel),
    path('payment/', views.payment),
    path('success/', views.success)
]
