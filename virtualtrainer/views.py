from django.shortcuts import render, redirect, get_object_or_404
from .models import MuscleGroup, Exercise

# Create your views here.


def virtualtrainer_home(request):
    return render(request, 'virtualtrainer/home.html')


def select_musclegroup(request):

    if request.method == "POST":
        muscle = request.POST.getlist('muscle')
        # form = SelectMusclesForm(request.POST, instance=muscle)
        # if muscle.is_valid():
        #     muscle = form.save(commit=False)
        #     muscle.save()
        return redirect('workout',)
    else:
    #     muscle = get_object_or_404(MuscleGroup, )
        return render(request, 'virtualtrainer/musclegroups.html')

def workout(request):
    workout = ['a', 'b']
    return render(request, 'virtualtrainer/workout.html', {'workout': workout})
