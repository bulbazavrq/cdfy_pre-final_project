from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='avatars/')
    specialization = models.CharField(max_length=255, blank=True)


class Role(models.Model):
    title = models.CharField(unique=True, max_length=255)
    access_level = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.title} [{self.access_level}]'

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
