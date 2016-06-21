from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.virtualtrainer_home, name='home'),
    url(r'^musclegroups/$', views.musclegroups, name='musclegroups'),
    url(r'^workout/$', views.workout, name='workout'),
]
