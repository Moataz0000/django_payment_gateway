from payment.domain.utilities.paymob_adapter import PaymobAdapter
from payment.domain.utilities.tap_adapter import TapAdapter
from payment.domain.enum import PaymentType




class PaymentGatewayFactory:
    
    @staticmethod
    def get_payment_gateway(gateway_type):
        if gateway_type == PaymentType.PAYMOB.value:
            return PaymobAdapter()
        elif gateway_type == PaymentType.TAP.value:
            return TapAdapter()
        else:
            raise ValueError(f"Unsupported payment gateway: {gateway_type}")