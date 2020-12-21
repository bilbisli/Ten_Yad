from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import User, Post
from django.utils.timezone import now, datetime
from django.contrib.auth.decorators import login_required
from .filters import PostSearch
from .forms import AssistOfferForm
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView


@login_required(login_url='/login/')
def homepage(request):
    posts = Post.objects.all()
    # show_posts = posts.order_by('-id')[:100]
    post_filter = PostSearch(request.GET, queryset=posts)
    show_posts = post_filter.qs
    context = {'page_title': 'homepage', 'show_posts': show_posts, 'post_filter': post_filter}
    return render(request, 'homepage/homepage.html', context)


@login_required(login_url='/login/')
def post_page(request):
    post_id = request.GET['id']
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {post_id}")
    return render(request, 'post/post.html', {'name': f'{post.title}', 'post': post})


@login_required(login_url='/login/')
def user_profile(request):
    user_id = request.GET['id']
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404(f"Invalid user id: {user_id}")

    rating = calculate_rating(user)

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


# @login_required(login_url='/login/')
def score_board(request):
    top_scores = sorted(User.objects.all(), key=lambda user: user.profile.points, reverse=True)[:5]
    top_scores = [(number + 1, user, calculate_rating(user)) for number, user in enumerate(top_scores)]

    score_board_link = 'scoreboard'
    context = {
        'top_scores': top_scores,
        'score_board_link': score_board_link
    }
    # return render(request, 'scoreboard.html')
    # posts = Post.objects.all()
    # # show_posts = posts.order_by('-id')[:100]
    # post_filter = PostSearch(request.GET, queryset=posts)
    # show_posts = post_filter.qs
    # context = {'page_title': 'homepage', 'show_posts': show_posts, 'post_filter': post_filter}
    return render(request, 'scoreboard/scoreboard.html', context)


def calculate_rating(user):
    try:
        return round(user.profile.rating_sum / user.profile.rating_count, 1)
    except ZeroDivisionError:
        return 0


def new_assist_post(request):
    if request.method == 'POST':
        assistance_form = AssistOfferForm(request.POST or None)
        if assistance_form.is_valid():
            assistance_form.instance.user = request.user
            form = assistance_form.save()
            # messages.success(request, f'New Post created!')
            return redirect('/')

        # assistance_form = AssistOfferForm(request.POST or None, instance=request.user)
        # if assistance_form.is_valid():
        #     saving = assistance_form.save(commit=False)
        #     saving.post.user = post.user
        #     saving.save()
        #     # messages.success(request, f'New Post created!')
        #     return redirect(f'/post?id={saving.post.id}')
    else:
        assistance_form = AssistOfferForm()
    context = {
        'form': assistance_form
    }
    return render(request, 'assist_offer/assist_offer.html', context)


def ReactView(request):
    post_id = request.GET['id']
    post = get_object_or_404(Post, id=post_id)
    post.reactions.add(request.user)
    return HttpResponseRedirect(reverse('post_page', args=[str(post_id)]))
