from django.conf.urls import url
from app import views
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.register_blogger, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),

]
