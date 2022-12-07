from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model


from PsychPhil_app.accounts.models import Profile

UserModel = get_user_model()

# When I have add_fieldsets and it finally works but i dunno why.
@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    list_display = ('email', 'is_staff', 'password', 'is_superuser', 'is_therapist', 'last_login', 'date_joined',)
    list_filter = ('is_staff',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email',
                           'password',
                           'is_staff',
                           'is_superuser',
                           'is_therapist',
                           'last_login',
                           'date_joined',
                           )}),
        ('Permissions', {
            'fields': ('groups', 'user_permissions'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('date_joined',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

# @admin.register(UserModel)
# class UserAdmin(auth_admin.UserAdmin):
#     add_form = SignUpForm
#
#
#
#     fieldsets = (
#         (
#             None,
#             {
#                 'fields': (
#                     'username',
#                     'password',
#                 ),
#             }),
#         (
#             'Personal info',
#             {
#                 'fields': (
#                     'first_name',
#                     'last_name',
#                     'self_summary',
#                     'image',
#                     'gender',
#                     'age',
#                     'user'
#                 ),
#             },
#         ),
#         (
#             'Permissions',
#             {
#                 'fields': (
#                     'is_active',
#                     'is_staff',
#                     'is_superuser',
#                     'groups',
#                     'user_permissions',
#                 ),
#             },
#         ),
#         (
#             'Important dates',
#             {
#                 'fields': (
#                     'last_login',
#                     'date_joined',
#                 ),
#             },
#         ),
#     )
#
#     def get_form(self, request, obj=None, **kwargs):
#         return super().get_form(request, obj, **kwargs)