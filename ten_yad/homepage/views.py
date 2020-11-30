from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import User, Post
from django.utils.timezone import now, datetime
from django.contrib.auth.decorators import login_required
from .filters import PostSearch


@login_required(login_url='/login/')
def homepage(request):
    posts = Post.objects.all()
    # show_posts = posts.order_by('-id')[:100]
    post_filter = PostSearch(request.GET, queryset=posts)
    show_posts = post_filter.qs
    context = {'page_title': 'homepage', 'show_posts': show_posts, 'post_filter': post_filter}
    return render(request, 'homepage/homepage.html', context)


@login_required(login_url='/login/')
def post(request):
    post_id = request.GET['id']
    try:
        post_ = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {post_id}")
    return render(request, 'post/post.html', {'name': f'{post_.title}', 'post': post_})


@login_required(login_url='/login/')
def user_profile(request):
    user_id = request.GET['id']
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404(f"Invalid user id: {user_id}")

    try:
        rating = round(user.profile.rating_sum / user.profile.rating_count, 1)
    except ZeroDivisionError:
        rating = 0
    if user.profile.birth_date.year:
        age = datetime.today().year - user.profile.birth_date.year
    else:
        age = None
    context = {
        'name': f'{user.username}',
        'user': user,
        'age': age,
        'rating': rating
    }
    return render(request, 'profile/profile.html', context)

