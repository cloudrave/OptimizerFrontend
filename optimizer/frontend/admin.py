from django.db import models
from django.contrib import admin

from frontend.models import *


class InputInline(admin.StackedInline):
    model = Input
    fields = ('name', 'order', 'default_value', 'description')

class FileInputInline(admin.StackedInline):
    model = FileInput
    fields = ('name', 'order', 'description')

class ProblemAdmin(admin.ModelAdmin):
    model = Problem
    inlines = [
        InputInline,
        FileInputInline,
    ]

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Algorithm)
