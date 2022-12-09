from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import *
from .models import *

# Create your views here.


def home(request):
    blogs = BlogModel.objects.all().order_by('-updated_at')
    lastest = blogs[0:3]
    context = {'blogs': blogs, 'lastest': lastest}
    return render(request, 'index.html', context)



def categories(request, cats):
    context = {'blogs': BlogModel.objects.filter(category=cats).all(), 'cat':cats.upper(),}
    return render(request, 'category.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        print(name, email, message)
        
        send_mail(f"Contact made by, {name}", message, email, ['testmail@gmail.com',])
        
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def login_user(request):
    # form = LoginForm()
    message = ''
    if request.method == "POST":
        username = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword')
        
        user = authenticate(
                username=username,
                password=password,
            )
        
        if user is not None:
            print(user)
            login(request, user)
            message = f'Hello {user.username}! You have been logged in'
            return redirect('home')
        else:
            message = 'Login failed!'
        
    return render(request, 'login.html',  context={'message': message})


def register(request):
    if request.method == "POST":
        username = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword')
        if Profile.objects.filter(username=username).exists():
            return render(request, 'register.html', {'message': 'Username already exists'})
        else:
            Profile.objects.create_user(username=username, password=password)
            
            user = authenticate(
                username=username,
                password=password,
            )
        
            if user is not None:
                print(user)
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                return redirect('home')
            else:
                message = 'Login failed!'
            
    return render(request, 'register.html')


@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login')
def add_blog(request):
 
    if request.method == 'POST' : # and request.FILES['image']
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_obj = form.save(commit=False)
            blog_obj.user = request.user
            # blog_obj.content = content
            blog_obj.save()
            
        return redirect('see-blog') 
        
    else:
        form = BlogForm()
 
    context = {'form': form}
    return render(request, 'add_blog.html', context)


@login_required(login_url='/login')
def blog_update(request, slug):
    context = {}

    blog_obj = BlogModel.objects.get(slug=slug)

    if blog_obj.user != request.user:
        return redirect('/')

    initial_dict = blog_obj
    form = BlogForm(instance=blog_obj)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog_obj)
   
        if form.is_valid():
            blog_obj = form.save(commit=False)
            blog_obj.user = request.user
            blog_obj.save()

            return redirect('see-blog')
        
    context['blog_obj'] = blog_obj
    context['form'] = form


    return render(request, 'update_blog.html', context)


def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = get_object_or_404(BlogModel, slug=slug)
        print(blog_obj)
        profile = Profile.objects.get(username = blog_obj.author)
        print(profile)
        comments = BlogComment.objects.filter(post=blog_obj).all()
        print(comments)
        replies = CommentReply.objects.all()
        print(replies)
        
        context['blog'] = blog_obj
        context['profile'] = profile
        context['comments'] = comments
        context['replies'] = replies
         
            
        if request.method == 'POST':
            
            comment = request.POST.get('comment')
            author = request.POST.get('author')
            email = request.POST.get('email')
            
            reply = request.POST.get('reply')
            reply_commentID = request.POST.get('replyedComment')
            
            print(reply_commentID)
               
            replyed_comment = BlogComment.objects.filter(id=reply_commentID).first()
         
            print(reply, replyed_comment)
            
            if comment and author:
                blogcom = BlogComment.objects.create(
                    post = blog_obj,
                    comment = comment,
                    name = author,
                    email = email
                )
                blogcom.save()
                
            if reply and replyed_comment:
                r = CommentReply.objects.create(
                    comment = replyed_comment,
                    reply = reply
                )
                r.save()
                
            return redirect('blog-detail', slug)
    except Exception as e:
        print(e)
    return render(request, 'detail_post.html', context)


@login_required(login_url='/login')
def see_blog(request):
    context = {}

    try:
        blog_objs = BlogModel.objects.filter(user=request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'see_blog.html', context)


@login_required(login_url='/login')
def blog_delete(request, slug):
    blog_obj = BlogModel.objects.get(slug=slug)
    print(blog_obj)

    if blog_obj.user == request.user:
        blog_obj.delete()

    return redirect('see-blog')

