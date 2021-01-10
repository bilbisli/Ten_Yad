from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth import login
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .decorators import account_activation_token
from django.core.mail import send_mail, BadHeaderError
from .forms import RegisterForm
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda user: not user.is_authenticated)
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your TenYad account.'
            message = render_to_string('register/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            try:
                send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])
            except BadHeaderError:
                raise Http404("Invalid header")

            return render(request, 'register/confirm_email.html')
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})


def activate(request, token, uidb64):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'register/html_email.html')
    else:
        return HttpResponse('Activation link is invalid!')