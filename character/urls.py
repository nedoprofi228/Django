from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('character/', views.about_character),
    path('weapons/<str:weapon_name>/', views.about_weapons),
    path('maps/', views.about_maps)
]
