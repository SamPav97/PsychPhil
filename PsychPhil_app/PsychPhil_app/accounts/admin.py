from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from PsychPhil_app.accounts.models import Profile

UserModel = get_user_model()


# Below are some necessary customization for Admin site to work with these models. When I have add_fieldsets it /
# finally works, but I am not sure why.
# A total of 5 customizations.
@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    search_fields = ("email__startswith",)
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
