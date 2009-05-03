# -*- coding: utf-8 -*-
#http://www.djangosnippets.org/tags/markup/
#mwlib
import re
from django.template.defaultfilters import stringfilter
from django import template

register = template.Library()



from creoleparser import text2html
@register.filter
@stringfilter
def wiki(text):
    return text2html(text)

if __name__ == '__main__':
