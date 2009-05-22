from django.db import models
from apkawa import settings
import mptt
import tagging
from django.template.defaultfilters import striptags

def wiki2html(text):
    from creoleparser import text2html
    return text2html( text, method='xhtml' )

def typograf(text):
    from typographus import typographus
    return typographus.typo( text )

def make_text(text):
    text = striptags( text )
    text = wiki2html( text )
    #text = typograf(text)
    return text

def title2slug(text):
    import pytils
    return pytils.translit.slugify(text)

class Post( models.Model):
    title = models.CharField( max_length=256)
    body_wiki = models.TextField()
    body_html = models.TextField(blank=True)

    author = models.ForeignKey( 'User', blank=True, null=True)
    slug = models.SlugField( max_length=256, editable=False)
    datetime_add = models.DateTimeField( auto_now = True)
    datetime_update = models.DateTimeField( auto_now = True, auto_now_add = True)
    edited_count = models.IntegerField(default=0, editable=False)
    category = models.ForeignKey('Category')
    tags_str = models.CharField( max_length=256, blank=True)
    #tags = models.ManyToManyField('Tag', blank=True,null=True)
    def __unicode__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.body_html = make_text( self.body_wiki )
        self.slug = title2slug( self.title )
        if not self.author:
            self.author = User.objects.get_or_create(
                    nick= settings.ADMINS[0][0],
                    email= settings.ADMINS[0][1] )[0]
        self.tags = self.tags_str
        if self.id:
            self.edited_count += 1
        super( Post, self).save(*args, **kwargs)
try:
    tagging.register( Post )
except tagging.AlreadyRegistered:
    pass


class Category( models.Model):
    title = models.CharField( max_length=256)
    slug = models.SlugField( max_length=256, blank=True, editable=False)
    #img = models.ImageField()
    def __unicode__(self):
        return self.title
    def save(self):
        self.slug = title2slug( self.title )
        super( Category, self).save()

class Tag( models.Model):
    title = models.CharField( max_length=256)
    slug = models.SlugField( max_length=256)
    def __unicode__(self):
        return self.title
    def save(self):
        self.slug = title2slug( self.title )
        super( Tag, self).save()

class Comment( models.Model):
    title = models.CharField( max_length=256)
    body_wiki = models.TextField()
    body_html = models.TextField(blank=True,editable=False)
    author = models.ForeignKey('User', blank=True, null=True)
    post = models.ForeignKey('Post')
    reply_to = models.ForeignKey('self', blank=True, null=True, editable=False)
    datetime_add = models.DateTimeField( auto_now = True)

    def __unicode__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.body_html = make_text( self.body_wiki )
        return super( Comment, self).save(*args, **kwargs)

try:
    mptt.register(Comment, order_insertion_by=['title',], parent_attr='reply_to')
except mptt.AlreadyRegistered:
    pass

class User( models.Model):
    nick = models.CharField( max_length=50)
    email = models.EmailField(blank=True)
    def __unicode__(self):
        return self.nick


# Create your models here.
