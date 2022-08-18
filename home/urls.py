from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('constant/<location>/', views.styles, name='ii'),
]