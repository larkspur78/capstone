from django.contrib import admin

# Register your models here.


from .models import MuscleGroup, Exercise
# Register your models here.
# takes in a model and registers it with admin interface
# we can use built-in django admin to create new instances of models
# when we import admin, it can have different sub-modules
# the site module is where you register new models


admin.site.register(MuscleGroup)
admin.site.register(Exercise)
