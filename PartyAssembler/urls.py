from django.conf.urls import include, url
from . import views


urlpatterns = [
     url(r'^$', views.home),
     url(r'^games$', views.games),
     url(r'^register/$', views.register, name="register"),
     url(r'^login/$', views.do_login, name="login"),
     url(r'^logout/$', views.do_logout, name="logout"),
     url(r'^user_profile/$', views.user_profile, name="user_profile"),
     url(r'^create_party/$', views.create_party, name="create_party"),
]
