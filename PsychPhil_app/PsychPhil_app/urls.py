
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PsychPhil_app.common.urls')),
    path('therapies/', include('PsychPhil_app.therapies.urls')),
    path('accounts/', include('PsychPhil_app.accounts.urls')),
    path('candidates/', include('PsychPhil_app.therapistCandidate.urls')),
]
