from django.conf.urls import include, url
from . import views


urlpatterns = [
     url(r'^$', views.home),
     url(r'^games$', views.games),
     url(r'^register/$', views.register, name="register"),
     url(r'^login/$', views.do_login, name="login"),
     url(r'^logout/$', views.do_logout, name="logout"),
     url(r'^profile/$', views.do_profile, name="profile"),
]
