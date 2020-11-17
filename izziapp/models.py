from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    product = models.CharField(max_length=500, verbose_name='product')
    date = models.DateField(verbose_name='order create date')


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_user', verbose_name='user')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='user_order', verbose_name='user_order')
    first_name = models.CharField(max_length=500, verbose_name='first_name')
    last_name = models.CharField(max_length=500, verbose_name='last_name')
    date = models.DateField(verbose_name='date of birth')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)