from email import message
from pyexpat.errors import messages
from django.shortcuts import render , redirect
from django.http import HttpResponse  
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout

from blog.models import blogpost 
from blog.models import blogpostForm , Comments

# Create your views here.
def home(request):
    return render(request,"blog/home.html")

def register(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password != password2:
            message.error(request, "Passwords do not match.")
            return render (request,"blog/register.html")
        
        else:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return render(request, 'blog/login.html')
    else:      
        return render(request, "blog/register.html")


def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return redirect("/blog")
        else:
            message.error(request, "Invalid Credentials")
           
    return render(request, "blog/login.html")


def profile(request):
    return render(request, "blog/profile.html")


def blogs(request):
    posts = blogpost.objects.all()
    posts = blogpost.objects.filter().order_by('-datetime')
    return render(request, "blog/blog.html", {'posts':posts})


def addblogs(request):
    
    if request.method=="POST":
        form =blogpostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.blogwriter = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(request, "blog/addblogs.html",{'obj':obj, 'alert':alert})
        
        else:
            return redirect("/blog/blogs")
        
    else:
        form=blogpostForm()
        return render(request, "blog/addblogs.html", {"form":form})
    
def blogs_comments(request, slug):
    post = blogpost.objects.filter(slug=slug).first()
    comments = Comments.objects.filter(blog=post)
    if request.method=="POST":
        user = request.user
        content = request.POST.get('blogcontent','')
        blog_id =request.POST.get('blog_id','')
        comment = Comments(commentauthor = user, blogcontent = content, blog=post)
        comment.save()
    return render(request, "blog_comments.html", {'post':post, 'comments':comments})

def Logout(request):
    logout(request)
     
    return redirect("/blog")

def about(request):
    return render(request, "blog/about.html")