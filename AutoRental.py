from typing import List, Optional
from datetime import date
from car import Car
from rental import Rental

class AutoRental:
    def __init__(self, name: str):
        self.name = name
        self.cars: List[Car] = []
        self.rentals: List[Rental] = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)

    def is_car_available(self, license_plate: str, rental_date: date) -> Optional[Car]:
        for car in self.cars:
            if car.license_plate == license_plate:
                if all(not (r.car.license_plate == license_plate and r.date == rental_date) for r in self.rentals):
                    return car
        return None

    def rent_car(self, license_plate: str, rental_date: date):
        if rental_date < date.today():
            print("Nem lehet múltbeli dátumra bérlést rögzíteni.")
            return

        car = self.is_car_available(license_plate, rental_date)
        if not car:
            print("Ez az autó nem elérhető bérlésre a megadott napon.")
            return

        new_rental = Rental(car, rental_date)
        self.rentals.append(new_rental)
        print(f"Sikeresen bérelted az autót {car.car_type} ({car.license_plate}) {car.rental_price} Ft-ért {rental_date}-én.")

    def cancel_rental(self, license_plate: str, rental_date: date):
        for rental in self.rentals:
            if rental.car.license_plate == license_plate and rental.date == rental_date:
                self.rentals.remove(rental)
                print(f"A(z) {license_plate} rendszámú autó {rental_date}-i bérlése lemondva.")
                return
        print("Nincs ilyen bérlés!")

    def list_rentals(self):
        if not self.rentals:
            print("Nincsenek aktív bérlések.")
        else:
            print("\nAktív bérlések:")
            for rental in sorted(self.rentals, key=lambda r: (r.date, r.car.license_plate)):
                print(" -", rental)
