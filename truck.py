from car import Car

class Truck(Car):
    def __init__(self, license_plate: str, car_type: str, rental_price: int, max_load: int, cargo_length: float):
        super().__init__(license_plate, car_type, rental_price)
        self.max_load = max_load  # kg
        self.cargo_length = cargo_length  # meters

    def __str__(self):
        return (
            f"Teherautó - {self.license_plate}, Típus: {self.car_type}, "
            f"Díj: {self.rental_price} Ft/nap, Teherbírás: {self.max_load} kg, "
            f"Rakodótér: {self.cargo_length} m"
        )
