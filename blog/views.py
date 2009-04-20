# Create your views here.
from apkawa.blog.models import Post, User, Category, Tag, Comment
from django.shortcuts import render_to_response
from django.http import  HttpResponseRedirect 


def main(request):
    posts = Post.objects.all().order_by('-datetime_add')[:5]
    return render_to_response('blog/main.html',{'posts':posts})

def post(request, slug):
    post = Post.objects.get( slug=slug)
    comments = Comment.objects.filter(post__id=post.id)
    return render_to_response('blog/post.html',{'post':post, 'comments':comments})

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

