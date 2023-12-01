from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('character/', views.all_characters),
    path('character/<str:character_name>/', views.about_character),
    path('weapons/', views.all_weapons),
    path('weapons/<str:weapon_name>/', views.about_weapons),
    path('maps/', views.all_maps),
    path('maps/<str:map_name>/', views.about_maps),
]
