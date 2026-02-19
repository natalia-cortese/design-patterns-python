# Adapter: Convert the interface of a class into another interface clients
# expect
# In this example the pattern was used to convert a legacy payment system into
# a new payment system.


class LegacyPaymentSystem:
    def pay(self, amount):
        print(f"Paying ${amount:.2f} with legacy payment system")
        return True

    def refund(self, amount):
        print(f"Refunding ${amount:.2f} with legacy payment system")
        return True


class NewPaymentSystem:
    def pay(self, amount):
        print(f"Paying ${amount:.2f} with new payment system")
        return True

    def refund(self, amount):
        print(f"Refunding ${amount:.2f} with new payment system")
        return True


class PaymentAdapter:
    def __init__(self, legacy_payment_system):
        self.legacy_payment_system = legacy_payment_system

    def pay(self, amount):
        return self.legacy_payment_system.pay(amount)

    def refund(self, amount):
        return self.legacy_payment_system.refund(amount)


# Example usage
if __name__ == "__main__":
    legacy_payment_system = LegacyPaymentSystem()
    new_payment_system = NewPaymentSystem()
    payment_adapter = PaymentAdapter(legacy_payment_system)
    print("--------------------------------")
    payment_adapter.pay(100)
    payment_adapter.refund(50)
    new_payment_system.pay(100)
    new_payment_system.refund(50)
    print("Legacy payment system:")
    legacy_payment_system.pay(100)
    legacy_payment_system.refund(50)
    print("New payment system:")
    new_payment_system.pay(100)
    new_payment_system.refund(50)
    print("Payment adapter:")
    payment_adapter.pay(100)
    payment_adapter.refund(50)
    print("--------------------------------")