from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_date')
    search_fields = ['title', 'post_content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('post_content')


# admin.site.register(Post, PostAdmin)
