from django.contrib import admin
from blog.xss.models import Blog, Category
from blog.xss.forms import ArticleModelAdminForm
from blog.xss.models import *


class BlogAdmin(admin.ModelAdmin):
    excluded = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    form = ArticleModelAdminForm


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
