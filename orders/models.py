from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from payment.models import Payment


class Order(models.Model):
    title = models.CharField(max_length=100, default='Some Order', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(default=timezone.now)
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT)
