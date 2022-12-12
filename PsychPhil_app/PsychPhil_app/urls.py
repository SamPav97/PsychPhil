from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from PsychPhil_app.exception_handler import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PsychPhil_app.common.urls')),
    path('therapies/', include('PsychPhil_app.therapies.urls')),
    path('accounts/', include('PsychPhil_app.accounts.urls')),
    path('candidates/', include('PsychPhil_app.therapistCandidate.urls')),
]

handler404 = page_not_found
handler500 = page_not_found

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# TODO i should create the view that accepts the file upload and check that it works.