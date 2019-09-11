from django.contrib import admin
from . import models
from posts.models import Post

class GroupMember_inline(admin.TabularInline):
    model = models.GroupMember
    extra = 1
class Post_inline(admin.StackedInline):
    model = Post
    extra = 1
class GroupAdmin(admin.ModelAdmin):
    inlines = (GroupMember_inline, Post_inline)

# Register your models here.
admin.site.register(models.Group, GroupAdmin)
#admin.site.register(models.GroupMember)