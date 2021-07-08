from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import  authenticate,login,logout
from django.contrib import messages
from django.views.generic import ListView,DetailView,CreateView
# Create your views here.
from datetime import datetime
#Create a form that an authenticated user can use to create a post.
from .models import Post


def user_login(request):
    if request.method== "POST":
        login_form = AuthenticationForm(request=request,data=request.POST)
        if(login_form.is_valid()):
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in sucessfully")
                return  HttpResponseRedirect('/post_page')

    else:
        login_form = AuthenticationForm()
    return render(request,'user/login.html',{'form': login_form})

# def post_page(request):
#     if request.user.is_authenticated :
#         return render(request,'user/post_page.html')
#     return HttpResponseRedirect('/')

class Postview(ListView):
    model = Post
    template_name = 'user/post_page.html'
class fullpost(DetailView):
    model = Post
    template_name = 'user/fullpost.html'
class addpost(CreateView):
    model = Post
    template_name = 'user/addpost.html'
    fields = 'user','text'

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')