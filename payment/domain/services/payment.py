from abc import ABC, abstractmethod



class PaymentGateway(ABC):
    @abstractmethod
    def proccess_payment(self, amount):
        pass    