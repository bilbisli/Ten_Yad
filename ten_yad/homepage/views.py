from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import User, Post
from django.utils.timezone import now


def homepage(request):
    recent_posts = Post.objects.filter().order_by('-id')[:100]
    return render(request, 'homepage/homepage.html', {'page_title': 'homepage', 'recent_posts': recent_posts})


def post(request):
    post_id = request.GET['id']
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {post_id}")
    return render(request, 'post/post.html', {'name': f'{post.title}', 'post': post})


def user_profile(request):
    user_id = request.GET['id']
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404(f"Invalid user id: {user_id}")
    return render(request, 'profile/profile.html', {'name': f'{user.name} {user.last_name} Profile', 'user': user})


def register(request):
    return render(request, 'register/homepage.html')


def register_user(request):
    new_user = User(
        username=request.POST['username'],
        password=request.POST['password'],
        time_registered=now(),
        name=request.POST['name'],
        last_name=request.POST['last_name'],
        birth_date=request.POST['last_name'],
        email=request.POST['email'],
        show_email=request.POST['show_email'],
        phone=request.POST['phone'],
        show_phone=request.POST['show_phone'],
        telegram=request.POST['telegram'],
        show_telegram=request.POST['show_telegram'],
        other_contact=request.POST['other_contact'],
        description=request.POST['description'],
        points=0
    )
    new_user.save()
    return render(request, '')




def login_user(request):
    return render(request, 'login')

