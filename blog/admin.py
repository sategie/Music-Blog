from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
# admin.site.register(Post, PostAdmin)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_date')
    search_fields = ['title', 'post_content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('post_content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'comment_content',
                    'created_date', 'approved')
    search_fields = ['name', 'created_date']
    list_filter = ('created_date', 'approved')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Function to approve selected comments
        """
        queryset.update(approved=True)
