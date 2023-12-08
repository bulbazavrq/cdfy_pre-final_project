from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, verbose_name='Телефон')
    address = models.CharField(max_length=255, blank=True, verbose_name='Адрес')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар')
    specialization = models.CharField(max_length=255, blank=True, verbose_name='Специализация')

    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )