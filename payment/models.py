from django.db import models
from django.contrib.auth.models import User

from .other.choices import PaymentMethod


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=2, choices=PaymentMethod.choices)
    total_amount = models.DecimalField(max_digits=14, decimal_places=2)
    is_paid = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.payment_method} - ${self.total_amount}"