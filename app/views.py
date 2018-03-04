from django.shortcuts import render
from django.views.generic import (TemplateView, ListView)
from app.forms import BloggerForm, BloggerProfileForm
# Create your views here.


class WelcomeView(TemplateView):
    template_name = 'app/welcome.html'


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
