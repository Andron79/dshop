from django.db import models
from django.contrib.auth.models import User

# from orders.models import Order


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50,  blank=True)
    # orders = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')

    class Meta:
        verbose_name = 'Профиль покупателя'
        verbose_name_plural = 'Профили покупателей'

    def __str__(self):
        return 'user {}'.format(self.user)