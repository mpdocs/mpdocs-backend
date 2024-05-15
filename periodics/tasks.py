from celery import shared_task
from django.contrib.auth import get_user_model

User = get_user_model()


@shared_task
def debug_task():
    print(User.objects.all())
