# Create your views here.
from apkawa.blog.models import Post, User, Category, Tag, Comment
from django.shortcuts import render_to_response
from django.http import  HttpResponseRedirect 

from django.forms import ModelForm
from django import forms

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

            new_comment = Comment.objects.get_or_create( title=title, body=body, post=post )
            return HttpResponseRedirect('/blog/post/%s/'%slug)


    return render_to_response('blog/post.html',{'post':post, 'comments':comments, 'add_comment':form})

def sorted( request, type, slug):
    print type, slug
    if type == 'tag':
        posts = Post.objects.filter( tags__slug = slug).order_by('-datetime_add')
    elif type == 'category':
        #cat = Category.objects.get( slug=slug)
        posts = Post.objects.filter( category__slug = slug).order_by('-datetime_add')
    if posts:
        return render_to_response('blog/main.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/blog/main/')

