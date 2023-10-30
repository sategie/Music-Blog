from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Post, Comment, Profile
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_date')
    search_fields = ['title', 'post_content']
    prepopulated_fields = {'slug': ('title', )}
    summernote_fields = 'post_content'


class CommentAdmin(admin.ModelAdmin):

    list_display = ('author', 'post', 'comment_content', 'created_date',
                    'approved')
    search_fields = ['author', 'created_date']
    list_filter = ('created_date', 'approved')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Function to approve selected comments
        """

        queryset.update(approved=True)


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'full_name')
    actions = ['delete_uploaded_profile_pic']

    def delete_profile_pic(self, request, queryset):
        """
        Function to remove uploaded profile pic
        """

        queryset.update(profile_pic=(
            'https://res.cloudinary.com/dvfxz4as6/image/upload/v1697302483/'
            'blank-profile-picture-973460_1280_skkwoi.png'
        ))


class UserAdmin(BaseUserAdmin):

    """
    Modifies the built-in User model to add 'is_staff' and 'is_superuser'
    which enables
    the creation of users with staff and superuser status in Django Admin.
    """

    # Fields used when creating a user

    add_fieldsets = ((None, {'classes': ('wide', ), 'fields': (
        'username',
        'email',
        'password1',
        'password2',
        'is_staff',
        'is_superuser',
        )}), )

    list_display = ('username', 'is_superuser')


# Register the new UserAdmin

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
