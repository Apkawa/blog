from apkawa.blog.models import Post, User, Category, Tag, Comment
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register( Post)


admin.site.register( User)
admin.site.register( Category)
admin.site.register( Tag)
admin.site.register( Comment)

