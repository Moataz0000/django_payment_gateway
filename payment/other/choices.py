from django.db import models




class PaymentMethod(models.TextChoices):
    PAYMOB = 'PM', 'Paymob'
    TAP = 'TP', 'Tap'

