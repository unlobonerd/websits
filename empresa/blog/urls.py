from django.urls import path
from . import views

urlpatterns = [

    path('', views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name="category"), # para acceder a la categoria
    
]