# Observer: Define a one-to-many dependency between objects so that when one
# object changes state, all its dependents are notified and
# updated automatically.
# In this example we define a observer for a weather station.


class WeatherStation:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)


class WeatherObserver:
    def update(self, temperature, humidity, pressure):
        pass


class WeatherDisplay (WeatherObserver):
    def update(self, temperature, humidity, pressure):
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure}hPa")  # noqa: E501


# Example usage
if __name__ == "__main__":
    weather_station = WeatherStation()
    weather_display = WeatherDisplay()
    weather_station.add_observer(weather_display)
    weather_station.notify_observers()
    print("--------------------------------")
    weather_station.remove_observer(weather_display)
    weather_station.notify_observers()
    print("--------------------------------")
