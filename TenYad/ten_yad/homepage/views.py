from django.shortcuts import render, redirect
from django.http import Http404
from .models import Message, Category
from django.utils.timezone import datetime, now
from django.contrib.auth.decorators import login_required
from .filters import PostSearch
from .forms import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail, BadHeaderError
from .forms import AssistOfferForm, EditProfile
from django.conf import settings


POINT_FOR_ASSIST = 10
SITE_ADRESS = 'http://127.0.0.1:8000'


@login_required(login_url='/login/')
def homepage(request):
    user = request.user
    posts = Post.objects.exclude(post_status=Post.PostStatus.ARCHIVE).order_by('time_updated_last')
    post_filter = PostSearch(request.GET, queryset=posts)
    show_posts = post_filter.qs
    context = {'page_title': 'homepage',
               'show_posts': show_posts[::-1],
               'post_filter': post_filter,
               'current_profile': request.user,
               'user': user,
               }
    return render(request, 'homepage/homepage.html', context)


@login_required(login_url='/login/')
def post_page(request):
    post_id = request.GET['id']
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {post_id}")
    context = {
        'current_profile': request.user,
        'name': f'{post.title}',
        'post': post,
        'user': request.user,
    }
    return render(request, 'post/post.html', context)


@login_required(login_url='/login/')
def edit_post(request):
    post_id = request.GET['id']
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {post_id}")
    if request.user.pk != post.user.pk:
        return redirect(f'/posts/post?id={post_id}')
    if request.method == 'POST':
        assistance_form = AssistOfferForm(request.POST, instance=post)
        if assistance_form.is_valid():
            assistance_form.instance.time_updated_last = now()
            form = assistance_form.save()
            return redirect(f'/posts/post?id={post_id}')
        else:
            return redirect(f'/')
    else:
        assistance_form = AssistOfferForm(instance=post)
    context = {
        'form': assistance_form,
        'current_profile': request.user,
    }
    return render(request, 'post/edit_post.html', context)


@login_required(login_url='/login/')
def user_profile(request):
    MAX_POINT = 200
    user_id = request.GET['id']
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404(f"Invalid user id: {user_id}")

    rating = calculate_rating(user)
    assist_count = calculate_assists_categories(user)
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
        'current_profile': request.user,
        'MAX_POINT': MAX_POINT,
        'Max_Assist': max(assist_count.values()),

    }
    return render(request, 'profile/profile.html', context)


@login_required(login_url='/login/')
def profile_edit(request):
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=request.user)
        form_user = EditUser(request.POST, instance=request.user)
        user = request.user
        if form.is_valid() and form_user.is_valid():
            form.save()
            form_user.save()
            return redirect(f"/user/profile?id={user.pk}")
    else:
        form = EditProfile(instance=request.user.profile)
        form_user = EditUser(instance=request.user)
    context = {
        'form': form,
        'formUser': form_user,
        'current_profile': request.user,
    }
    return render(request, 'profile/editProfile.html', context)


@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        user = request.user
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(f"/user/profile?id={user.pk}")
    else:
        form = PasswordChangeForm(user=request.user.profile)
    return render(request, 'profile/change_password.html', {'form': form, 'current_profile': request.user})


@login_required(login_url='/login/')
def score_board(request):
    top_scores = sorted(User.objects.all(), key=lambda user: user.profile.points, reverse=True)[:100]
    top_scores = [(number + 1, user, calculate_rating(user)) for number, user in enumerate(top_scores)]

    score_board_link = 'scoreboard'
    context = {
        'top_scores': top_scores,
        'score_board_link': score_board_link,
        'current_profile': request.user,
    }
    return render(request, 'scoreboard/scoreboard.html', context)


@login_required(login_url='/login/')
def new_assist_post(request):
    if request.method == 'POST':
        assistance_form = AssistOfferForm(request.POST or None)
        if assistance_form.is_valid():
            user = request.user
            post = assistance_form.instance
            post.user = user
            form = assistance_form.save()
            send_alert(user, f"You created a post: '{post.title}'", f"/posts/post?id={post.pk}", False)
            return redirect(f"/posts/post?id={post.pk}")
    else:
        assistance_form = AssistOfferForm()
    context = {
        'form': assistance_form,
        'current_profile': request.user,
    }
    return render(request, 'assist_offer/assist_offer.html', context)


@login_required(login_url='/login/')
def ReactView(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {pk}")
    user = request.user
    post.reactions.add(user)
    user_post = post.user
    send_alert(user_post, f"New reaction to your post: '{post.title}' from {request.user}", f"/posts/post?id={pk}")
    send_alert(user, f"You reacted to post: '{post.title}'", f"/posts/post?id={pk}", False)
    return redirect(f'/posts/post?id={pk}')


@login_required(login_url='/login/')
def CancelReactView(request, pk, user_reaction_remove, redirection=None):
    print("lets see")
    if not redirection:
        redirection = f'/posts/post?id={pk}'
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {pk}")
    # post = Post.objects.get(id=post_id)
    user = User.objects.get(id=user_reaction_remove)
    if post.user.pk == request.user.pk or request.user.pk == user_reaction_remove:
        if user in post.reactions.all():
            post.reactions.remove(user)
        if user in post.approved_reactions.all():
            post.approved_reactions.remove(user)
            if not post.approved_reactions.all():
                post.post_status = Post.PostStatus.ACTIVE

    return redirect(redirection)


@login_required(login_url='/login/')
def AcceptReactView(request, pk, approved_reaction):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {pk}")
    user = User.objects.get(id=approved_reaction)
    if request.user.pk == post.user.pk:
        if not post.approved_reactions.all() or post.post_type == post.PostType.GROUP_ASSIST_OFFER or post.post_type == post.PostType.GROUP_ASSIST_REQUEST:
            post.approved_reactions.add(user)
            post.post_status = Post.PostStatus.TRANSACTION
        else:
            return redirect(f'/posts/post?id={pk}')
        post.approved_reactions.add(user)
        post.post_status = Post.PostStatus.TRANSACTION
        send_alert(user, f"Your assist in: '{post.title}' was accept by {post.user.profile} - "
                         f"contact details now appear on the post -click to view-", link=f"/posts/post?id={pk}")
    return redirect(f'/posts/post?id={pk}')


@login_required(login_url='/login/')
def CompleteAssistView(request, pk, user_assist, redirection=None):
    if not redirection:
        redirection = f'/posts/post?id={pk}'
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {pk}")
    user = User.objects.get(id=user_assist)
    if request.user.pk == post.user.pk:
        post.users_assist.add(user)
        add_points(user=user, amount=POINT_FOR_ASSIST)
        msg = f"Your assist in: '{post.title}' was approved {POINT_FOR_ASSIST}" \
              f" points added to your score congratulations!!"
        send_alert(user=user, message=msg, link=f"/posts/post?id={pk}")
        if post.category:
            get_icon(user, post.category.name)
        if user in post.reactions.all():
            post.reactions.remove(user)
        if user in post.approved_reactions.all():
            post.approved_reactions.remove(user)
        post.users_to_rate.add(user)
        post.reacted_user_rate.add(user)
    return redirect(redirection)


@login_required(login_url='/login/')
def rate_user_view(request, pk, user_rate, amount_rate):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {pk}")
    current_profile = request.user
    if current_profile.pk != user_rate and (post.user.pk == current_profile.pk or current_profile in post.reacted_user_rate.all()):
        user = User.objects.get(id=user_rate)
        user.profile.rating_sum += amount_rate
        user.profile.rating_count += 1
        user.profile.save()
        if current_profile.pk == post.user.pk:
            post.users_to_rate.remove(user)
        else:
            post.reacted_user_rate.remove(current_profile)
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
    if request.user.pk == post.user.pk:
        post.post_status = Post.PostStatus.ACTIVE
        post.save()
    return redirect(f'/posts/post?id={pk}')


@login_required(login_url='/login/')
def DeletePostView(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404(f"Invalid post id: {pk}")
    if request.user.pk == post.user.pk:
        post.delete()
    return redirect(f'/posts/history')


@login_required(login_url='/login/')
def post_history(request):
    user = request.user
    context = {
        'name': f'{user.username}',
        'user': user,
        'user_posts': Post.objects.all().filter(user=user),
        'current_profile': request.user,
    }
    return render(request, 'profile/post_history.html', context)


@login_required(login_url='/login/')
def Messages(request):
    user = request.user
    read_notifications = list(reversed(user.notifications.all()))
    unread_notifications = []
    if user.profile.unread_notifications:
        unread_notifications = read_notifications[:user.profile.unread_notifications]
        read_notifications = read_notifications[user.profile.unread_notifications:]
    unread_notifications = [(number + 1, notification) for number, notification in enumerate(unread_notifications)]
    read_notifications = [(number + 1, notification) for number, notification in enumerate(read_notifications)]
    context = {
        'user': user,
        'unread_notifications': unread_notifications,
        'read_notifications': read_notifications,
        'current_profile': request.user,
    }
    user.profile.unread_notifications = 0
    user.profile.save()
    return render(request, 'messages/messages.html', context)


def certificate(request):
    user_id = request.GET['id']
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404(f"Invalid user id: {user_id}")
    if user.profile.certificate:
        context = {
            'current_profile': request.user,
            'user': user,
        }
        return render(request, 'certificate/certificate.html', context)
    return redirect('/')


@login_required(login_url='/login/')
def SearchVolunteersView(request):
    user = request.user
    if user.profile.is_representative:
        category = request.POST.get('category')
        print(category)
        number = request.POST.get('number')
        if number:
            number = int(number)

        # category = request.GET['category']
        # number = int(request.GET['number'])

        users = []
        if number and category != 'None':
            for user in User.objects.all():
                assist_category = calculate_assists_categories(user)
                if category in assist_category and assist_category[category] >= number:
                    users.append(user)
        potential_v = request.GET.getlist('pot_vol')
        if request.method == 'POST':
            form = ContactEmailForm()
        else:
            form = ContactEmailForm(request.GET)
            if form.is_valid():
                subject = "Volunteering opportunity from TenYad: "
                subject = subject + form.cleaned_data['subject']
                message = f"A message was sent from Ten Yad - user (ID {user.pk}): {user.profile} ({user.email})\n"
                message = message + form.cleaned_data['message']
                for potential_volunteer in potential_v:
                    potential_volunteer = User.objects.get(id=potential_volunteer)
                    try:
                        send_mail(subject, message, user.email, [potential_volunteer.email])
                    except BadHeaderError:
                        raise Http404("Invalid header")
                    send_alert(
                        user=potential_volunteer,
                        message=f'New volunteering opportunity from {user.profile} - check your email for further details',
                        link=f'/user/profile?id={user.pk}'
                    )
                send_alert(
                    user=user,
                    message=f"you're email '{subject}' was sent to all potential volunteers")
                return redirect('/volunteers')
        context = {
            'searchVolunteers': users,
            'user': user,
            'categories': Category.objects.all(),
            'current_profile': request.user,
            'form': form,
            'category': category,
        }
        return render(request, 'searchVolunteers/searchVolunteers.html', context)
    return redirect('/')


@login_required(login_url='/login/')
def contact_admin(request):
    user = request.user
    if request.method == 'GET':
        form = ContactEmailForm()
    else:
        form = ContactEmailForm(request.POST)
        if form.is_valid():
            subject = "Ten Yad Contact Admin: "
            subject = subject + form.cleaned_data['subject']
            message = f"A message was sent from Ten Yad - user (ID {user.pk}): {user.profile} ({user.email})\n"
            message = message + form.cleaned_data['message']
            try:
                send_mail(subject, message, request.user.email, [settings.EMAIL_HOST_USER])
            except BadHeaderError:
                raise Http404("Invalid header")
            send_alert(
                user=user,
                message=f"you're email '{subject}' was sent to admin")
            return redirect('/')
    context = {
        'form': form,
        'current_profile': user,
    }
    return render(request, "contact_admin/contact_admin.html", context)


def calculate_rating(user):
    try:
        return round(user.profile.rating_sum / user.profile.rating_count, 1)
    except ZeroDivisionError:
        return 0


def send_alert(user, message, link=None, alert=True):
    msg = Message(user=user)
    msg.link = link
    msg.notification = message
    msg.save()
    if alert:
        user.profile.unread_notifications += 1
    user.profile.save()


def check_send_certificate(user):
    if not user.profile.certificate:
        if user.profile.points > 250:
            user.profile.certificate = True
            send_alert(user, f"Congratulations you have won a certificate of appreciation, "
                             f"please check your email !", link=f"/certificate?id={user.pk}")
            res = send_mail('Congratulations you have won a certificate of appreciation from "Ten-Yad"',
                            f'{SITE_ADRESS}/certificate?id={user.pk}',
                            settings.EMAIL_HOST_USER, [user.email])


def add_points(user, amount):
    user.profile.points += amount
    user.profile.save()
    check_send_certificate(user)


def calculate_assists_categories(user):
    assist_count = {k.name: 0 for k in Category.objects.all()}
    assist_count['No Category'] = 0

    for post in filter(lambda some_post: user in some_post.users_assist.all(), Post.objects.all()):
        if not post.category:
            assist_count['No Category'] += 1
        else:
            assist_count[post.category.name] += 1
    return assist_count


def get_icon(user, category):
    category = str(category)
    assist_count = calculate_assists_categories(user)
    max_category = 0
    for k, v in assist_count.items():
        if max_category < v and k != category:
            max_category = v

    if category in assist_count.keys() and assist_count[category] > max_category:
        if user.profile.points >= 50 and assist_count[category] == 3:
            send_alert(user, "Congratulations you have won a new trophy", f"/user/profile?id={user.pk}")
        if user.profile.points >= 100 and assist_count[category] == 5:
            send_alert(user, "Congratulations you have won a new trophy", f"/user/profile?id={user.pk}")
        if user.profile.points >= 200 and assist_count[category] == 7:
            send_alert(user, "Congratulations you have won a new trophy", f"/user/profile?id={user.pk}")
