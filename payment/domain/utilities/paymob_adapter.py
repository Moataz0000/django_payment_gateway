from payment.domain.services.payment import PaymentGateway



class PaymobAdapter(PaymentGateway):
    def proccess_payment(self, amount):
        print(f"Processing ${amount} through Paymob Gateway.")
        # Integrate with Paymob API here
    




