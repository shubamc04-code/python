from abc import ABC , abstractmethod

class Vehicle(ABC):
	"""Real-world example: every vehicle must define how it starts."""

	@abstractmethod
	def start(self):
		pass


class Car(Vehicle):
	def start(self):
		return "Car starts with a key or button"


class ElectricCar(Vehicle):
	def start(self):
		return "Electric car starts silently"


vehicles = [Car(), ElectricCar()]
for vehicle in vehicles:
	print(vehicle.start())
    