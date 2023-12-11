from django.db import models

# Create your models here.


class Role(models.Model):
    title = models.CharField(unique=True, max_length=255)
    access_level = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.title} [{self.access_level}]'

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
