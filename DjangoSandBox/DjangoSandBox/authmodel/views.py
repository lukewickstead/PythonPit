from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from authmodel.forms import UserForm, UserLoginForm


def index(request):
    return render(request, 'authmodel/index.html')


@login_required
def users(request):
    """
    You can surround the view in url with login_require(my_view.as_view()) but this is much nicer.

    Directs to settings.LOGIN_URL
    """

    return render(request, 'authmodel/users.html', {"users": User.objects.all()})


def logout_page(request):
    logout(request)
    return render(request, 'authmodel/logout.html')


def login_page(request):
    form = UserLoginForm(request.POST or None)

    if request.POST and form.is_valid():
        username = form.cleaned_data["login"]
        password = form.cleaned_data["password"]

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)

            if request.GET.get('next') is not None:
                return redirect(request.GET['next'])
            else:
                return redirect(reverse('auth:index'))

    return render(request, 'authmodel/login.html', {'form': form})


def create_login(request):
    form = UserForm(request.POST or None)

    if request.POST and form.is_valid():
        email = form.cleaned_data['email']
        user_login = form.cleaned_data['login']
        password = form.cleaned_data['password']
        last_name = form.cleaned_data['last_name']
        first_name = form.cleaned_data['first_name']

        new_user = User.objects.create_user(username=user_login, email=email, password=password,
                                            first_name=first_name, last_name=last_name)

        new_user.is_active = True
        new_user.save()

        # Password can be changed with
        # new_user.set_password("new_pw")
        # new_user.save()

        return redirect(reverse('auth:index'))

    return render(request, 'authmodel/create_login.html', {'form': form})
