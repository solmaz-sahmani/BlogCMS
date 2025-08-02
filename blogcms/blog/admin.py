from django.contrib import admin
from .models import Post, Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_date')
    list_filter = ('created_date', 'category')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}