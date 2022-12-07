from django.contrib import admin

from PsychPhil_app.therapistCandidate.models import TherapistCand


@admin.register(TherapistCand)
class TherpyAdmin(admin.ModelAdmin):
    pass
