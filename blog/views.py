# Create your views here.
from apkawa.blog.models import Post, User, Category, Tag, Comment
from django.shortcuts import render_to_response
from django.http import  HttpResponseRedirect

from django.forms import ModelForm
from django import forms

from tagging.models import Tag, TaggedItem


class CommentForm(forms.Form):
    body = forms.CharField(max_length=2048, widget=forms.Textarea)
    title = forms.CharField( max_length = 256)
    #author = forms.CharField( max_length=140)



def main(request):
    posts = Post.objects.all().order_by('-datetime_add')[:5]
    return render_to_response('blog/main.html',{'posts':posts})

def post(request, slug):
    post = Post.objects.get( slug=slug)
    comments = Comment.objects.filter(post__id=post.id)

    form = CommentForm()
    if request.POST:
        add_comment = request.POST
        title = add_comment['title']
        body = add_comment['body']
        if body:
            if not title:
                title = u'Re: %s'%post.title

            new_comment = Comment.objects.create( title=title, body_wiki=body, post=post )
            return HttpResponseRedirect('/blog/post/%s/'%slug)


    return render_to_response('blog/post.html',{'post':post, 'comments':comments, 'add_comment':form})

def category( request, slug):
    posts = Post.objects.filter( category__slug = slug).order_by('-datetime_add')
    if posts:
        return render_to_response('blog/main.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/blog/main/')

def tag( request, id):
    tag = Tag.objects.get( id = id )
    posts = TaggedItem.objects.get_union_by_model( Post, tag)
    #posts = Post.objects.filter( tags__slug = slug).order_by('-datetime_add')
    if posts:
        return render_to_response('blog/main.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/blog/main/')
