from django.db import models

class Post( models.Model):
    title = models.CharField( max_length=256)
    body = models.TextField()
    author = models.ForeignKey( 'User')
    slug = models.SlugField( max_length=256)
    datetime_add = models.DateTimeField( auto_now = True)
    datetime_update = models.DateTimeField( auto_now = True, auto_now_add = True)
    edited_count = models.IntegerField(default=0)
    category = models.ForeignKey('Category')
    tags = models.ManyToManyField('Tag', blank=True,null=True)
    def __unicode__(self):
        return self.title


class Category( models.Model):
    title = models.CharField( max_length=256)
    slug = models.SlugField( max_length=256)
#    img = models.PictureField()
    def __unicode__(self):
        return self.title

class Tag( models.Model):
    title = models.CharField( max_length=256)
    slug = models.SlugField( max_length=256)
    def __unicode__(self):
        return self.title

class Comment( models.Model):
    title = models.CharField( max_length=256)
    body = models.TextField()
    author = models.ForeignKey('User', blank=True, null=True)
    post = models.ForeignKey('Post')
    reply_to = models.ForeignKey('self', blank=True, null=True)
    datetime_add = models.DateTimeField( auto_now = True)

    def __unicode__(self):
        return self.title

class User( models.Model):
    nick = models.CharField( max_length=50)
    email = models.EmailField(blank=True)
    def __unicode__(self):
        return self.nick


# Create your models here.
