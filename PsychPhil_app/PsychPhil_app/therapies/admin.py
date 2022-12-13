from django.contrib import admin
from PsychPhil_app.therapies.models import Therapy


@admin.register(Therapy)
class TherpyAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)
