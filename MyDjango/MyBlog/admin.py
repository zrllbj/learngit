#coding=utf-8
from django.contrib import admin
from .models import *
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','pub')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','category','content','pub')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog','name','content','pub')


admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Blog,BlogPostAdmin)
admin.site.register(Comment,CommentAdmin)