from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recommend/', views.save_user, name='save_user'),
    path('recommend/complete', views.recommend, name='recommend'),
    path('plantCreate/', views.plantCreate, name='plantCreatePage'),
    path('plantCreate/create', views.Create_Plant, name='plantCreate'),
]
