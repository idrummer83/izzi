from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    product = models.CharField(max_length=500, verbose_name='product')
    date = models.DateField(verbose_name='order create date')

    def __str__(self):
        return '{}'.format(self.product)


class Customer(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='user_order', verbose_name='user_order', blank=True, null=True)
    first_name = models.CharField(max_length=500, verbose_name='first_name')
    last_name = models.CharField(max_length=500, verbose_name='last_name')
    date_birthday = models.DateField(verbose_name='date of birth')
    date_register = models.DateField(verbose_name='date of order')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)