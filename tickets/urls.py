from django.conf.urls import url, include
from tickets import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^landing/$', views.landing, name='landing'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^(?P<pk>[0-9])+/$', views.ticket_detail, name='ticket_detail'),
]
