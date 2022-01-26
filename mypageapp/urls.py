from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'mypageapp'

urlpatterns = [
    path('user/<int:id>/', views.update_user, name = 'update_user'),

    path('user/<int:id>/pet/', views.create_pet, name ='create_pet'),

    # path('show/<int:id>/', views.show, name ='show'),
    path('update/<int:id>/', views.update_pet, name='update_pet'),


]