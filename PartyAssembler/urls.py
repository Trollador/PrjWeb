from django.conf.urls import include, url
from . import views


urlpatterns = [
     url(r'^$', views.home, name="home"),
     url(r'^games$', views.games, name="games"),
     url(r'^register/$', views.register, name="register"),
     url(r'^login/$', views.do_login, name="login"),
     url(r'^logout/$', views.do_logout, name="logout"),
     url(r'^create_party/$', views.create_party, name="create_party"),
     url(r'^alt-profile/$', views.reg_profile, name="alt-profile"),
     url(r'^profile/$', views.profile, name= "profile"),
     url(r'^games/parties/(?P<pk>[0-9]+)/$', views.parties_detail, name = "parties_detail"),
     url(r'^parties/(?P<pk>[0-9]+)$', views.enter_party, name = "enter_party"),
     url(r'^parties/$', views.parties, name="parties"),
     url(r'^post/$', views.Post, name='post'),
     url(r'^messages/$', views.Messages, name='messages'),
     url(r'^chat/$', views.chatTemplate, name='home'),
     url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.users_profile),
]
