from django.contrib import admin
from example.forms import StandardModelForm, StandardModelTwoForm
from example.models import *


class StandardModelTwoInline(admin.StackedInline):
    model = StandardModelTwo
    form = StandardModelTwoForm


class StandardModelAdmin(admin.ModelAdmin):
    model = StandardModel
    inlines = [StandardModelTwoInline]
    form = StandardModelForm


admin.site.register(StandardModel, StandardModelAdmin)
