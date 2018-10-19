from django.contrib import admin
from myblog.models import Blog, Category, Tag, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'click_nums', 'category', 'create_time', 'modify_time']


admin.site.register(Comment)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)
# Register your models here.
