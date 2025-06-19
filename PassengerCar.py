from car import Car

class PassengerCar(Car):
    def __init__(self, license_plate: str, car_type: str, rental_price: int, seat_count: int, has_ac: bool):
        super().__init__(license_plate, car_type, rental_price)
        self.seat_count = seat_count
        self.has_ac = has_ac

    def __str__(self):
        ac_status = "van klíma" if self.has_ac else "nincs klíma"
        return (
            f"Személyautó - {self.license_plate}, Típus: {self.car_type}, "
            f"Díj: {self.rental_price} Ft/nap, Ülések: {self.seat_count}, {ac_status}"
        )
