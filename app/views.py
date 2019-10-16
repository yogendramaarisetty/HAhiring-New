from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token
import smtplib


def register1(request):
    """Renders the Registration page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/register.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
      
    )
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('register')
    else:
        return render(request, 'app/account_activation_invalid.html')
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('register')
    else:
        form = SignUpForm()
    return render(request, 'app/register.html', {'form': form})

def signup(request):
    print("************")
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your your test'
            message = render_to_string('app/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            print(user.email)
            print(user)
            # user.email_user(subject, message)
            send_email(subject, message, user.email)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'app/register.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'app/account_activation_sent.html')

def send_email(subject, msg, to_add):
    to="167r1a05m4@gmail.com"
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login("yogendramaarisetty@gmail.com", "yyyooogggiii1")
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail("yogendramaarisetty@gmail.com", to_add, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")