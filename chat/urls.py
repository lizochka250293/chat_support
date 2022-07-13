from django.urls import path
from . import views
# from .views import NumberFormView
from .views import AddStarRating
urlpatterns = [
    # path('', views.index, name='title'),
    path('api/number_create/', views.NumberCreateApiView.as_view(), name='number_api'),
    path('add-rating/', views.AddStarRating.as_view, name='add_rating'),
    path('', views.NumberFormView.as_view(), name='title'),
    path('number/<str:room_name>/', views.PersonalArea.as_view(), name='index'),
    # path('number/<str:room_name>/', views.number, name='index'),
    # path('chat/<str:room_name>/', views.room, name='room'),
    path('chat/<str:room_name>/', views.PersonalRoom.as_view(), name='room')

]
