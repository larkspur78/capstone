from django.shortcuts import render, redirect, get_object_or_404
from .models import MuscleGroup, Exercise

# Create your views here.


def virtualtrainer_home(request):
    return render(request, 'virtualtrainer/home.html')


def select_musclegroup(request):
    return render(request, 'virtualtrainer/musclegroups.html')
