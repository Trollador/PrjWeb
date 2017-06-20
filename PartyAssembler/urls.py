from django.conf.urls import include, url
from . import views


urlpatterns = [
     url(r'^$', views.home),
     url(r'^games$', views.games),
     url(r'^register/$', views.register, name="register"),
     url(r'^login/$', views.do_login, name="login"),
     url(r'^logout/$', views.do_logout, name="logout"),
     url(r'^create_party/$', views.create_party, name="create_party"),
     url(r'^alt-profile/$', views.reg_profile, name="alt-profile"),
     url(r'^profile/$', views.profile, name= "profile"),
     url(r'^profile_others/$', views.profile_others, name= "profile_others"),
     url(r'^games/parties/(?P<pk>[0-9]+)/$', views.parties_detail, name = "parties_detail"),
     url(r'^parties/(?P<pk>[0-9]+)$', views.enter_party, name = "enter_party"),
     url(r'^parties/$', views.parties, name="parties"),
     url(r'^post/$', views.Post, name='post'),
     url(r'^messages/$', views.Messages, name='messages'),
     url(r'^chat/$', views.chatTemplate, name='home'),
]
