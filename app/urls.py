from django.conf.urls import url
from app import views
urlpatterns = [
    url(r'^$', views.WelcomeView.as_view(), name='welcome'),
    url(r'^register/$', views.register_blogger, name='register')
]
