# -*- coding: utf-8 -*-
from django.template.defaultfilters import truncatewords_html, wordcount
from django import template

register = template.Library()


@register.inclusion_tag('blog/templatetags/post_tag.html')
def make_post( post, turncate=False ):
    if turncate:
        turncate = int(turncate)
        if wordcount(post.body_html) >= turncate:
            post.body_html = truncatewords_html(post.body_html, turncate)
        else:
            turncate = False
    return {'post':post, 'turncate' : turncate }

if __name__ == '__main__':
    pass
