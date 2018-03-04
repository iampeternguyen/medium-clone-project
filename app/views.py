from django.shortcuts import render
from django.views.generic import (TemplateView, ListView)
from app.forms import BloggerForm, BloggerProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


class IndexView(TemplateView):
    template_name = 'app/index.html'


def register_blogger(request):
    registered = False

    if request.method == 'POST':
        user_form = BloggerForm(data=request.POST)
        profile_form = BloggerProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = BloggerForm()
        profile_form = BloggerProfileForm()
    return render(request, 'app/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse("invalid login details")

    else:
        return render(request, 'app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
