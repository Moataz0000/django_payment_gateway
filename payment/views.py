from django.shortcuts import render
from payment.domain.factory import PaymentGatewayFactory




PaymentGatewayFactory.get_payment_gateway(gateway_type='tap')