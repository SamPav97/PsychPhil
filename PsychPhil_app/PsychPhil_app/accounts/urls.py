from django.urls import path, include

from PsychPhil_app.accounts.views import SignInView, SignUpView, SignOutView, UserDetailsView, UserUpdateView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('details/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('update/', UserUpdateView.as_view(), name='update user'),
    ])),
)
