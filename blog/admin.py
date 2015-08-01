from django.contrib import admin
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin





class PostAdmin(SummernoteModelAdmin):
	fields = ['title', 'slug', 'body', 'category']
	prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)