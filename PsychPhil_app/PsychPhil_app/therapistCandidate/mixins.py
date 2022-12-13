from django.contrib.auth.mixins import AccessMixin


# I probably rewrote some default mixin to adjust it to my purpose.
class NonTherapistRequiredMixin(AccessMixin):
    """Verify that the current user is not a therapist."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_therapist:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class TherapistRequiredMixin(AccessMixin):
    """Verify that the current user is a therapist."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_therapist:
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()

