from django.urls import path, include
from . import views



urlpatterns=[
    path('', views.home),
    path('recipes/', views.homeView ),
     path('recipes/<str:tribe>', views.homeView ),
    path('recipe/<str:id>', views.recipeDetails),
    path('create/', views.createView),
]