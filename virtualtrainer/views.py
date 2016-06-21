from django.shortcuts import render, redirect, get_object_or_404
from .models import MuscleGroup, Exercise
import random

# Create your views here.


def virtualtrainer_home(request):
    """
    Generates webpage displaying title of project and call to action

    **Template**

    :template:`virtualtrainer/home.html`

    """
    return render(request, 'virtualtrainer/home.html')


def musclegroups(request):
    """
    Generates webpage displaying musclegroups images with clickable regions

    **Template**

    :template:`virtualtrainer/musclegroups.html`

    """

    template_location = 'virtualtrainer/musclegroups.html'
    return render(request, template_location,)

    # muscle = request.POST.getlist('muscle')
    # # print(muscle)
    # context = {
    #     # filters out any posts that can contain the query that we've searched
    #     # 'musclegroups': 'muscles'
    #     'exercises': Exercise.objects.filter(musclegroup__name__in=muscle)
    # }

def workout(request):
    """
    Displays a workout routine as a list of four exercise items

    **Context**

    ``exercises``
        A randomized list of exercises, instance of :model:`Exercise`

    **Template**

    :template:`virtualtrainer/workout.html`

    """
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
