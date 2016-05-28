from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.virtualtrainer_home, name='home'),
    url(r'^musclegroups/$', views.select_musclegroup, name='musclegroups'),
    # url(r'^workout/$', views.return_workout, name='workout'),
]
