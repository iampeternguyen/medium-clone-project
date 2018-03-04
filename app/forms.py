from django import forms
from django.contrib.auth.models import User
from app.models import BloggerProfile


class BloggerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class BloggerProfileForm(forms.ModelForm):
    class Meta():
        model = BloggerProfile
        fields = ('bio', 'avatar')
