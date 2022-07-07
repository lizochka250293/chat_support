from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='title'),
    path('number/<str:room_name>/', views.number, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
]
