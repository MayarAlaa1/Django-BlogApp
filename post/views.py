# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.

# from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from BlogApp.models import Post,Category,Tag,Comment,Likes
from AccountsApp.models import ExtendedUser
from django.conf import settings
from .forms import *
from django.contrib.auth.models import User

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login as authlogin
User = settings.AUTH_USER_MODEL
def category(request):
	category=Post.objects.all()
	context={'category':category}
	return render (request,'post/category.html',context)

def post(request, post_id):
    all_categories= Category.objects.all()
    post=get_object_or_404(Post,pk=post_id)
    all_Tags= Tag.objects.all()
	# is_liked = False
	# if post.likes.filter(id=request.User.id).exists():
	# 	is_liked = True


    comments=Comment.objects.filter(postId=post.postId , reply=None)
    if request.method =='POST':
        comment_form=CommentForm(request.POST or None)
        if comment_form.is_valid():
            content=request.POST.get('commentContent')
            reply_id=request.POST.get('comment_id')
            comment_qs=None
            if reply_id:
                comment_qs=Comment.objects.get(commentId=reply_id)
            comment=Comment.objects.create(postId=post,commentAuthor=request.user , commentContent=content , reply=comment_qs)
            comment.save()
            comment_form = CommentForm()

    else : 
        comment_form=CommentForm()  

    context={
    'post':post,
    'all_categories':all_categories,
    'all_Tags':all_Tags,
    'category':category,
    'comments': comments,
    # 'new_comment': new_comment,
    'comment_form': comment_form,
# 'is_liked':is_liked,
# 'total_likes':post.total_likes(),


    }
    return render (request,'post/post.html',context)


def category_detail(request, cat_id):
    category = get_object_or_404(Category,pk=cat_id)
    post= Post.objects.filter(postCategory=cat_id).order_by('-postDatePublished')
    return render(request,'post/list.html', {
        'category': category,
        'post':post,
    })

def like(request,post_id):
    if not Likes.objects.filter(pId=post_id, User=request.user.id).exists():
        post = Post.objects.get(postId=post_id)

        if request.POST.get('like') == '1':
            Likes.objects.create(pId=post, User=request.user, likes = True)
        else:
            Likes.objects.create(pId=post, User=request.user, likes = False)

        like = Likes.objects.filter(pId=post, likes = 0)

        if like.count() >= 10:
            like.delete()
            post.delete()

    return HttpResponseRedirect('/post/post/' + post_id)