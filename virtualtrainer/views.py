from django.shortcuts import render, redirect, get_object_or_404
from .models import MuscleGroup, Exercise
import random

# Create your views here.


def virtualtrainer_home(request):
    return render(request, 'virtualtrainer/home.html')


def search(request):
    # muscle = request.POST.getlist('muscle')
    # # print(muscle)
    # context = {
    #     # filters out any posts that can contain the query that we've searched
    #     # 'musclegroups': 'muscles'
    #     'exercises': Exercise.objects.filter(musclegroup__name__in=muscle)
    # }
    template_location = 'virtualtrainer/musclegroups.html'
    return render(request, template_location,)


def workout(request):
    if request.method == "POST":
        muscle = request.POST.getlist('muscle')
        exercises = list(Exercise.objects.filter(musclegroup__name__in=muscle))

        context = {
            'exercises': random.sample(exercises, 4)
        }
        return render(request, 'virtualtrainer/workout.html', context)
        # {'workout': Exercise.objects.filter(musclegroup__name__in=muscle)})


# def select_musclegroup(request):
#
#     if request.method == "GET":
#         muscle = request.GET.getlist('muscle')
#         # form = SelectMusclesForm(request.POST, instance=muscle)
#         # if muscle.is_valid():
#         #     muscle = form.save(commit=False)
#         #     muscle.save()
#         return redirect('workout',)
#     else:
#     #     muscle = get_object_or_404(MuscleGroup, )
#         return render(request, 'virtualtrainer/musclegroups.html')
#
