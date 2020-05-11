from django.shortcuts import render, get_object_or_404
from .models import Post, Category #importamos el modelo osea la tabla donde estan el contenido
# Create your views here.

def blog(request):
    post = Post.objects.all()
    return  render(request, "blog/blog.html", {'post':post})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id) #filtra por el campo id, de la gtabal de Category y reotrna 404 si no existe
    return render(request, "blog/category.html", {'category':category})
