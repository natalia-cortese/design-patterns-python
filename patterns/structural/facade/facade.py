# Facade: Provide a simplified interface to a complex system.
# In this example the pattern was used to build a payment processor that
# can be used to pay and refund with different payment methods.


class CreditCardPayment:
    def authorize(self, card_number, amount):
        # Simulated: check card number, check funds, hold amount
        print(f"Authorizing credit card {card_number} for ${amount:.2f}")
        return True

    def capture(self, card_number, amount):
        # Simulated: capture previously authorized amount
        print(f"Capturing ${amount:.2f} on card {card_number}")
        return True

    def refund(self, card_number, amount):
        # Simulated: perform refund
        print(f"Refunding ${amount:.2f} to card {card_number}")
        return True


class PaypalPayment:
    def login(self, email, password):
        print(f"Logging into PayPal account {email}")
        return True

    def pay(self, email, amount):
        print(f"Paying ${amount:.2f} using PayPal account {email}")
        return True

    def refund(self, email, amount):
        print(f"Refunding ${amount:.2f} to PayPal account {email}")
        return True


class CryptoPayment:
    def connect_wallet(self, address):
        print(f"Connecting to crypto wallet {address}")
        return True

    def transfer(self, address, amount, currency):
        print(f"Transferring {amount} {currency} from wallet {address}")
        return True

    def refund(self, address, amount, currency):
        print(f"Refunding {amount} {currency} to wallet {address}")
        return True


# Facade
class PaymentProcessor:
    def __init__(self):
        self.credit_card = CreditCardPayment()
        self.paypal = PaypalPayment()
        self.crypto = CryptoPayment()

    def pay_with_credit_card(self, card_number, amount):
        if self.credit_card.authorize(card_number, amount):
            return self.credit_card.capture(card_number, amount)
        return False

    def pay_with_paypal(self, email, password, amount):
        if self.paypal.login(email, password):
            return self.paypal.pay(email, amount)
        return False

    def pay_with_crypto(self, address, amount, currency):
        if self.crypto.connect_wallet(address):
            return self.crypto.transfer(address, amount, currency)
        return False

    def refund_credit_card(self, card_number, amount):
        return self.credit_card.refund(card_number, amount)

    def refund_paypal(self, email, amount):
        return self.paypal.refund(email, amount)

    def refund_crypto(self, address, amount, currency):
        return self.crypto.refund(address, amount, currency)


# Example usage
if __name__ == "__main__":
    processor = PaymentProcessor()
    print('\n--- Payment Examples ---')
    processor.pay_with_credit_card("4111-1111-1111-1111", 99.99)
    processor.pay_with_paypal("user@example.com", "password123", 49.99)
    processor.pay_with_crypto("0xABCDEF123456", 1.5, "ETH")

    print('\n--- Refund Examples ---')
    processor.refund_credit_card("4111-1111-1111-1111", 10)
    processor.refund_paypal("user@example.com", 5)
    processor.refund_crypto("0xABCDEF123456", 0.3, "ETH")