from apkawa.blog.models import Post, User, Category, Tag, Comment
from django.contrib import admin

class CommentInline(admin.TabularInline):
    model = Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'tags_str']
    inlines = [
            CommentInline,
            ]
    pass

admin.site.register( Post, PostAdmin)


admin.site.register( User)
admin.site.register( Category)
admin.site.register( Tag)

admin.site.register( Comment)
