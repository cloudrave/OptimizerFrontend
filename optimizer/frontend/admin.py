from django.db import models
from django.contrib import admin

from frontend.models import *


class InputInline(admin.StackedInline):
    model = Input
    fields = ('name', 'order', 'description')

class ProblemAdmin(admin.ModelAdmin):
    inlines = [
        InputInline,
    ]

class VariableInline(admin.StackedInline):
    model = Variable

class AlgorithmAdmin(admin.ModelAdmin):
    inlines = [
        VariableInline,
    ]

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Algorithm, AlgorithmAdmin)
