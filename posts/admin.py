from django.contrib import admin
from posts.models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'created_at',)
    list_filter = ('category', 'user',)
    search_fields = ('title', 'content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'created_at',)
    list_filter = ('user', 'created_at',)
    search_fields = ('content',)