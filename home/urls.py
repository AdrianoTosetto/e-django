from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<oid>\d$)', views.index, name='whatever'),
    url(r"^(\d+)/(\d+)$", views.requestMessages, name="requestMessages"),
    url(r"^(?P<u1>\d+)/(?P<u2>\d+)/(?P<msg>[\w\-]+)/$", views.insertNewMessage, name="insertNewMessage"),
    url(r"^countUnreadMessages/(?P<userId>\d+)/(?P<idSent>\d+)/", views.countUnreadMessages, name="insertNewMessage"),
    url(r'^requestFrieds/(?P<userId>\d+)/', views.requestFriends, name='requestFriends'),
 	url(r'^login', views.login, name="login"),
 	url(r'^cad', views.addUser, name="cad"),
    url(r'^', views.helper, name="home"),
]