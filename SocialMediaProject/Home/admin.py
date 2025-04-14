from django.contrib import admin
from .models import Post, Comment, Profile

admin.site.register(Post)


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created', 'is_reply')
    raw_id_fields = ('user', 'post', 'reply')


admin.site.register(Profile)
