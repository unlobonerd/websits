from django.contrib import admin
from .models import Category, Post  #se importan los modelos o tablas

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):  #se crea una clase para dar acceso de solo lectura a lso campos de fecha
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories') #para ver lso campos en el panel de administracion en columnas, dentro de entradas
    ordering = ('author', 'published')    #para ordenar
    search_fields = ('title', 'author__username', 'categories__name')  #por ser una tupla se debe dejar la coma al fina si solo es un objeto, cuando se busque con campos relaciones s debe colcar dos _ y el campo
    date_hierarchy = 'published' #para orgazir por jerarquia de ffchas
    list_filter = ('author__username',) # para ver el campo de filtro al lado derecho
    
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")]) #dentro de la clase post_ junta y busca todos los objetos
    post_categories.short_description = "Categorias" #para mostrar en la fila el nombre de categoria en lugar de post_categories


admin.site.register(Category, CategoryAdmin) #se registran par poder verlos desde el panel de adminsitacion
admin.site.register(Post, PostAdmin)
