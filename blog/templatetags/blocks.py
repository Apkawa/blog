from django import template
from apkawa.blog.models import Post, User, Category, Tag
from django.shortcuts import render_to_response

register = template.Library()
@register.inclusion_tag('blog/templatetags/left_block.html')
def left_block():
    categorys= Category.objects.all()
    tags = Tag.objects.all()
    return {'tags':tags,'categorys':categorys,}

    

