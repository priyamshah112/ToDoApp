from django.shortcuts import render,redirect
from .models import Posts
from .forms import PostForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
	posts_list = Posts.objects.order_by('id')
	
	form = PostForm()

	context = {'posts_list' : posts_list,'form':form}

	return render(request,'posts/index.html',context)

@require_POST
def addPost(request):
	form = PostForm(request.POST)
	print(request.POST['title'],request.POST['description'],request.POST['status'])
	if form.is_valid():
		new_todo = Posts(title=request.POST['title'],description=request.POST['description'],status=request.POST['status'])
		new_todo.save()
	return redirect('index')

@require_POST
def updatePost(request,id):
	todoid = Posts.objects.get(id=id)
	form = PostForm(request.POST)
	print(request.POST['title'],request.POST['description'],request.POST['status'])
	if form.is_valid():
		new_todo = Posts(id=id,title=request.POST['title'],description=request.POST['description'],status=request.POST['status'])
		new_todo.save()
	return redirect('index')

@require_POST
def deletePost(request,id):
	todoid = Posts.objects.get(id=id)
	form = PostForm(request.POST)
	if request.method=='POST':
		todoid.delete()
	return redirect('index')


def displayPost(request, posts_id):
	form = PostForm()
	todoid = Posts.objects.get(pk=posts_id)

#	todo_title =Posts.objects.get(posts_title)
#	todo_description = Posts.objects.get(description)
#	todo_status = Posts.objects.get(status)

#	print(todoid,todo_title,todo_description,todo_status)
#	context = {'todoid' : todoid ,'todo_title' : todo_title,'todo_description' : todo_description,'todo_status' : todo_status }
	context = {'todoid' : todoid,'form':form}
	return render(request,'posts/display.html',context)
	
