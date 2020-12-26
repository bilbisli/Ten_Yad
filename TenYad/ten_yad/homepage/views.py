from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import User, Post
from django.utils.timezone import now, datetime
from django.contrib.auth.decorators import login_required
from .filters import PostSearch
from .forms import AssistOfferForm, EditProfile
from django.urls import reverse

from django.template import loader

from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserChangeForm


@login_required(login_url='/login/')
def homepage(request):
    posts = Post.objects.exclude(post_status=Post.PostStatus.ARCHIVE)
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
    return render(request, 'post/post.html', {'name': f'{post.title}', 'post': post, 'user': request.user})


@login_required(login_url='/login/')
def user_profile(request):
    MAX_POINT = 200
    user_id = request.user.pk
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404(f"Invalid user id: {user_id}")

    rating = calculate_rating(user)

    if user.profile.birth_date and user.profile.birth_date.year:
        age = datetime.today().year - user.profile.birth_date.year
    else:
        age = None
    context = {
        'name': f'{user.username}',
        'user': user,
        'user_posts': Post.objects.all().filter(user=user),
        'age': age,
        'rating': rating,
        'MAX_POINT': MAX_POINT,
    }
    return render(request, 'profile/profile.html', context)


@login_required(login_url='/login/')
def profile_edit(request):
    args = {}
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=request.user)
        user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = EditProfile()

    args['form'] = form
    return render(request, 'profile/editProfile.html', args)


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def ReactView(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {pk}")
    # post = Post.objects.get(id=post_id)
    post.reactions.add(request.user)
    return redirect(f'/posts/post?id={pk}')


@login_required(login_url='/login/')
def CancelReactView(request, pk, user_reaction_remove):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {pk}")
    # post = Post.objects.get(id=post_id)
    user = User.objects.get(id=user_reaction_remove)
    if user in post.reactions.all():
        post.reactions.remove(user)
    if user in post.approved_reactions.all():
        post.approved_reactions.remove(user)
        if not post.approved_reactions.all():
            post.post_status = Post.PostStatus.ACTIVE
    return redirect(f'/posts/post?id={pk}')


@login_required(login_url='/login/')
def AcceptReactView(request, pk, approved_reaction):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {pk}")
    post.approved_reactions.add(User.objects.get(id=approved_reaction))
    post.post_status = Post.PostStatus.TRANSACTION
    return redirect(f'/posts/post?id={pk}')


@login_required(login_url='/login/')
def CompleteAssistView(request, pk, user_assist):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {pk}")
    user = User.objects.get(id=user_assist)
    post.users_assist.add(user)
    if user in post.reactions.all():
        post.reactions.remove(user)
    if user in post.approved_reactions.all():
        post.approved_reactions.remove(user)
    return redirect(f'/posts/post?id={pk}')


@login_required(login_url='/login/')
def ClosePostView(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {pk}")
    post.post_status = Post.PostStatus.ARCHIVE
    post.save()
    return redirect('/')


@login_required(login_url='/login/')
def ReactivatePostView(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {pk}")
    post.post_status = Post.PostStatus.ACTIVE
    post.save()
    return redirect(f'/posts/post?id={pk}')


@login_required(login_url='/login/')
def DeletePostView(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {pk}")
    post.delete()
    return redirect(f'/posts/history')


@login_required(login_url='/login/')
def post_history(request):
    user = request.user
    context = {
        'name': f'{user.username}',
        'user': user,
        'user_posts': Post.objects.all().filter(user=user),
    }
    return render(request, 'profile/post_history.html', context)


def Messages(request):
    user = request.user
    context = {
        'reactions': Post.reactions,
        'rating_sum': user.profile.rating_sum,
        'points': user.profile.points,
    }
    return render(request, 'messages/messages.html', context)




