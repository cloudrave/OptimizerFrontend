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

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Algorithm)
