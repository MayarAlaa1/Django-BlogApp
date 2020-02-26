from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as authlogin
from .models import Post
from django.db.models import Q 
from django.http import HttpResponse
# Create your views here.

def home(request):

	# query: get all posts
	topPosts= Post.objects.all().order_by('date')[:5] 
	
	# query: get count of comments

	# query to get path of image or image name 
	

	context ={
	"topPosts": topPosts
	}
	return render(request ,'BlogApp/index.html' , context)


def post(request,id):
	# post = post.objects.get(id=id)
	# query = request.GET.get("q,None")
	# qs = Post.objects.all()
	# if query is not None:
	# 	qs = qs.filter(
	# 		Q(title__icontains=query)

	# 	).distinct()
	

	context = {
				'id':id,
				#'object_list': qs,
	}

	return render(request,'BlogApp/post.html',context)

def search(request):
	query = request.GET.get("query")
	#qs = Post.objects.all()
	if query :
		qs = Post.objects.filter(
			Q(title__icontains=query)|Q(tags__tagname__icontains=query) 

		).distinct()
			
		# ts =Tag.objects.filter(
		# 	Q(tagname__icontains=query)

		# ).distinct() 

	

	context = {
				'object_list': qs,
	}

	return render(request,'BlogApp/post.html',context)


def category(request):
	context = {

	}
	return render (request,'BlogApp/category.html', context)

def blocked(request):
	context = {

	}
	return render (request, 'BlogApp/blocked.html', context)

def register(request):
	if request.method == 'POST':

		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username = username, password = password)
			authlogin(request,user)
			return redirect('home')
	else:

		form = UserCreationForm()
	context = {

		'form':form
	}
	return render(request ,'registration/register.html' , context)


def login(request):
	context = {
	
	}
	return render(request ,'BlogApp/login.html' , context)

def showpost(request,num):
	post=Post.objects.get(postId=num)
	return render(request,'BlogApp/post.html',{'post':post})


	
# def toggle(request):
#     w = user.objects.get(id=request.POST['id'])
#     w.is_working = request.POST['isworking'] == 'true'
#     w.save()
#     return HttpResponse('success')