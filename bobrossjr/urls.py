from django.conf.urls import url
from bobrossjr import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^birthday_list/$', views.birthday_list, name='birthday_list')
]