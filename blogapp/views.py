from django.shortcuts import render,redirect
from.models import Blog
from django.contrib import messages
from django.contrib.auth.models import auth,User
from .forms import ModeForm
# Create your views here.
def fun(request):
    blog=Blog.objects.all()
    return render(request,"index.html",{'blogs':blog})
def add_blog(request):
    if request.method == "POST":
        img = request.FILES["img"]
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        author = request.POST.get("author")
        # date = request.POST.get("date")
        s = Blog(img=img,title=title,desc=desc,author=author)
        s.save()
    return render(request,"add_blog.html")


def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('blogapp:fun')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,"login.html")
def register(request):
    if request.method=="POST":
        fname = request.POST["firstname"]
        lname = request.POST["lastname"]
        uname = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST["password1"]
        pass2 = request.POST["password2"]
        if pass1==pass2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username already exist!!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist!!")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pass1)
                user.save();
                messages.info(request,"user created")
                return redirect('blogapp:fun')
        else:
            messages.info(request,"password not matched")
            return redirect('register')
    else:
        return render(request,"registration.html")
def logout(request):
    auth.logout(request)
    return redirect('blogapp:fun')

def update(request,id):
    obj=Blog.objects.get(id=id)
    form=ModeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('blogapp:fun')
    return render(request,"edit.html",{'form':form,'obj':obj})

def delete(request,id):
    if request.method=="POST":
        obj=Blog.objects.get(id=id)
        obj.delete()
        return  redirect('blogapp:fun')
    return  render(request,"delete.html")