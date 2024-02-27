from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ReportTemplate(models.Model):
    """
    Модель для хранения шаблонов docx отчётов
    """

    # пока не уверен, нужно ли оно будет
    name = models.TextField(
        verbose_name="Название шаблона",
        help_text="Введите название шаблона",
    )
    template_file = models.FileField(
        upload_to="report_templates",
        verbose_name="Файл шаблона",
        help_text="Загрузите файл шаблона в формате docx",
    )
    version = models.CharField(
        max_length=255,
        verbose_name="Версия",
        help_text="Введите версию шаблона, например, v1",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Шаблон отчёта"
        verbose_name_plural = "Шаблоны отчётов"

    def __str__(self):
        return f"Отчёт {self.name} - {self.version}"

    def __repr__(self):
        return (
            f"ReportTemplate(name={self.name}, "
            f"version={self.version}, "
            f"created_at={self.created_at}, "
            f"updated_at={self.updated_at})"
        )


class Report(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,  # хотим хранить отчёты, даже если пользователь удалён
        verbose_name="Пользователь",
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Отчёт"
        verbose_name_plural = "Отчёты"

    def __str__(self):
        return f"Отчёт пользователя {self.user.username} от {self.created_at}"

    def __repr__(self):
        return f"Report(user={self.user}, created_at={self.created_at}, updated_at={self.updated_at})"
