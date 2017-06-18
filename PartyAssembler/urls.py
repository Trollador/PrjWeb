from django.conf.urls import include, url
from . import views


urlpatterns = [
     url(r'^$', views.home),
     url(r'^games$', views.games),
     url(r'^register/$', views.register, name="register"),
     url(r'^login/$', views.do_login, name="login"),
     url(r'^logout/$', views.do_logout, name="logout"),
     url(r'^create_party/$', views.create_party, name="create_party"),
     url(r'^games/parties/(?P<pk>[0-9]+)/$', views.parties_detail, name = "parties_detail"),
     url(r'^alt-profile/$', views.reg_profile, name="alt-profile"),
    #url(r'^parties/$', views.parties, name="parties"),
]
