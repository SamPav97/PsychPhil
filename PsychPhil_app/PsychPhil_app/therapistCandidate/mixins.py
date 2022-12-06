from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

from PsychPhil_app.therapistCandidate.models import TherapistCand


class NonTherapistRequiredMixin(AccessMixin):
    """Verify that the current user is not a therapist."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_therapist:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class TherapistRequiredMixin(AccessMixin):
    """Verify that the current user is not a therapist."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_therapist:
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()


# class ApplicationInProcessMixin(AccessMixin):
#     """Verify that the current user is not a therapist."""
#
#     def dispatch(self, request, *args, **kwargs):
#         try:
#             candidate = TherapistCand.objects \
#                 .filter(user_id=request.user.id) \
#                 .get()
#         except TherapistCand.DoesNotExist:
#             candidate = None
#
#         if candidate:
#             # done (I just made the check in the view n temp n display sth diff if alrdy candidate) make return a view where it says u in process
#             return redirect('index')
#         return super().dispatch(request, *args, **kwargs)