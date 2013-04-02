from django.contrib import admin
from test_project.forms import StandardModelForm, StandardModelTwoForm
from test_project.models import *


class StandardModelTwoInline(admin.StackedInline):
    model = StandardModelTwo
    form = StandardModelTwoForm


class StandardModelAdmin(admin.ModelAdmin):
    model = StandardModel
    inlines = [StandardModelTwoInline]
    form = StandardModelForm


admin.site.register(StandardModel, StandardModelAdmin)
