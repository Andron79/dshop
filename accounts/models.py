from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #email = models.EmailField(max_length=50, unique=True, blank=False)
    city = models.EmailField(max_length=50,  blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return 'user {}'.format(self.id)