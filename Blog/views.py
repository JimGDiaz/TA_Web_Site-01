from django.shortcuts import render
from Blog.models import Categoria, Post

# Create your views here.

def blog(request):
    posts= Post.objects.all()
    return render(request, "Blog/blog.html", {"posts_tmp": posts})

def categoria(request, categoria_id):
    categoria_f = Categoria.objects.get(id=categoria_id) # Todas las Categorias con ese id
    post_f = Post.objects.filter(categorias=categoria_f) # Todos los Post de esa Categoria
    return render(request, "Blog/categoria.html", {"categoria_filtro": categoria_f, "post_filtro":post_f})