from django import template

register = template.Library()
'''
Formated
**полужирный** - <strong>полужирный</strong>
//курсив// - <em>курсив</em>
__подчеркнутый__ - <u>подчеркнутый</u>
--зачеркнутый-- - <s>зачеркнутый</s>
##моноширинный## - <tt>моноширинный</tt>
++Мелкий текст++ - <small>Мелкий текст</small>
http://code.djangoproject.com/wiki/CookBookTemplateFilterBBCode
http://dumpz.org/127/
'''
@register.filter("wiki")
def dokuwiki_filter( text ):
    pass


