from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


# admin.site.unregister(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
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
