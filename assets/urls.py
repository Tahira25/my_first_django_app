from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name= 'assets'),
    #path('<int:assest_id', views.asset, name= 'asset'),
    #path('search', views.search, name= 'search'),
]
