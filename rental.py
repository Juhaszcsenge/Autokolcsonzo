from datetime import date
from car import Car

class Rental:
    def __init__(self, car: Car, rental_date: date):
        self.car = car
        self.date = rental_date

    def __str__(self):
        return f"{self.date} - {self.car}"
