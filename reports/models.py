from django.contrib.auth import get_user_model
from django.db import models
import django.utils.timezone
from django_stubs_ext.db.models import TypedModelMeta

from reports import utils
from reports.managers import ReportTemplateManager

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

    is_active = models.BooleanField(
        verbose_name="Активен ли шаблон", default=False, null=False, blank=False
    )

    report_start_date = models.DateTimeField(
        verbose_name="Дата начала отчетного периода",
        default=django.utils.timezone.now
    )

    report_end_date = models.DateTimeField(
        verbose_name="Дата окончания отчетного периода",
        default=django.utils.timezone.now
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ReportTemplateManager()

    def __str__(self):
        return f"Шаблон отчёта {self.name}"

    def __repr__(self):
        return (
            f"ReportTemplate(name={self.name}, "
            f"created_at={self.created_at}, "
            f"updated_at={self.updated_at}"
            f"report_start_date={self.report_start_date}"
            f"report_end_date={self.report_end_date})"
        )

    class Meta(TypedModelMeta):
        verbose_name = "Шаблон отчёта"
        verbose_name_plural = "Шаблоны отчётов"


class Report(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,  # хотим хранить отчёты, даже если пользователь удалён
        verbose_name="Пользователь",
        null=True,
    )
    template = models.ForeignKey(
        ReportTemplate,
        on_delete=models.SET_NULL,  # хотим хранить отчёт, даже если кто-то удалил темплейт
        verbose_name="Шаблон, по которому заполняется отчет",
        null=True,
    )
    data = models.JSONField(
        verbose_name="Содержание отчета",
        null=True,  # сомнительно
        encoder=utils.DateTimeEncoder,
    )

    is_reviewed = models.BooleanField(
        null=False,
        blank=False,
        default=False,
        verbose_name="Просматривал ли отчет модератор",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Отчёт пользователя {self.user.username} от {self.created_at}"

    def __repr__(self):
        return f"Report(user={self.user}, created_at={self.created_at}, updated_at={self.updated_at})"

    class Meta(TypedModelMeta):
        verbose_name = "Отчёт"
        verbose_name_plural = "Отчёты"
