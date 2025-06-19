from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, license_plate: str, car_type: str, rental_price: int):
        self.license_plate = license_plate
        self.car_type = car_type
        self.rental_price = rental_price

    @abstractmethod
    def __str__(self):
        pass
