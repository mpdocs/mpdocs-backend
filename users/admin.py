from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'patronymic')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'patronymic', 'password')


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    fieldsets = (
        (
            "Аккаунт",
            {
                "fields": (
                    "username",
                    "email",
                )
            },
        ),
        (
            "Конфиденциальная информация",
            {"fields": ("password",)},
        ),
        (
            "Персональная информация",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "patronymic",
                )
            },
        ),
        (
            "Права доступа",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Важные даты",
            {"fields": ("last_login", "date_joined")},
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'patronymic', 'is_staff',
                    'is_superuser', 'groups', 'user_permissions'),
            },
        ),
    )

    list_display = (
        "id",
        "username",
        "email",
        "last_name",
        "first_name",
        "patronymic",
    )
    list_display_links = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "patronymic",
    )

    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
        "patronymic",
    )

    list_filter = (
        "is_staff",
        "is_superuser",
    )
