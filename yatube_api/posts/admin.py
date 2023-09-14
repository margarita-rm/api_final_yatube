from django.contrib import admin

from posts.models import Comment, Follow, Group, Post

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Follow)
