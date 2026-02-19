# Strategy: Define a family of algorithms, encapsulate each one,
# and make them interchangeable.
# In this example we define a strategy for different transport methods.


class Transport:
    def __init__(self, name):
        self.name = name

    def transport(self):
        pass


class TransportStrategy:
    def __init__(self, transport):
        self.transport = transport

    def transport(self):
        return self.transport.transport()


class TransportStrategyFactory:
    def __init__(self):
        self.strategies = {}

    def register_strategy(self, name, strategy):
        self.strategies[name] = strategy

    def get_strategy(self, name):
        return self.strategies[name]


class CarStrategy (TransportStrategy):
    def transport(self):
        return "Driving a car"


class TrainStrategy (TransportStrategy):
    def transport(self):
        return "Taking a train"


class PlaneStrategy (TransportStrategy):
    def transport(self):
        return "Flying a plane"


# Example usage
if __name__ == "__main__":
    transport_strategy_factory = TransportStrategyFactory()
    transport_strategy_factory.register_strategy("car", CarStrategy())
    transport_strategy_factory.register_strategy("train", TrainStrategy())
    transport_strategy_factory.register_strategy("plane", PlaneStrategy())
    transport_strategy = transport_strategy_factory.get_strategy("car")
    print(transport_strategy.transport())
    transport_strategy = transport_strategy_factory.get_strategy("train")
    print(transport_strategy.transport())
    transport_strategy = transport_strategy_factory.get_strategy("plane")
    print(transport_strategy.transport())
    print("--------------------------------")
