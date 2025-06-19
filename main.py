from datetime import date
from rental import Rental
from PassengerCar import PassengerCar
from truck import Truck
from tenant import Tenant
from AutoRental import AutoRental  

def setup_system() -> AutoRental:
    rental_company = AutoRental("Credit Car rendtal") 

    print("--- Kezdeti bérlések ---")
    tenant1 = Tenant("Lakatos Nina")    
    tenant2 = Tenant("Szoboszlai Csilla")
    tenant3 = Tenant("Kovács Kinga")
    tenant4 = Tenant("Berrei Enikő")
    tenant5 = Tenant("Turcsányi Lajos")

    rental_company.add_car(PassengerCar("JKL-321", "Mazda 3", 8800, 5, True))
    rental_company.add_car(PassengerCar("XYZ-654", "Volkswagen Golf", 9200, 5, False))
    rental_company.add_car(Truck("TRK-999", "Iveco Daily", 16000, 2000, 4.0))
    rental_company.add_car(PassengerCar("AGDH-124", "Mazda 6", 8800, 5, True))
    rental_company.add_car(PassengerCar("HJK-732", "Volkswagen PASSAT", 9200, 3, False))
    rental_company.add_car(Truck("OLP-286", "Ford Focus", 16000, 2000, 4.0))

    print("--- Új bérlések rögzítése ---")
    rental_company.rent_car("JKL-321", date(2025, 6, 20))
    rental_company.rent_car("XYZ-654", date(2025, 6, 21))
    rental_company.rent_car("TRK-999", date(2025, 6, 22))
    rental_company.rent_car("XYZ-654", date(2025, 6, 21))  
    rental_company.rent_car("AAA-111", date(2025, 6, 24))  
    rental_company.rent_car("JKL-321", date(2024, 5, 15))  

    print("---------------------------")
    return rental_company


def user_interface(rental_company: AutoRental):
    while True:
        print("\n--- Autókölcsönző rendszer ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Aktív bérlések listázása")
        print("4. Kilépés")
        choice = input("Válassz egy lehetőséget: ")

        if choice == "1":
            license_plate = input("Add meg a bérelni kívánt autó rendszámát: ").upper()
            date_str = input("Add meg a bérlés dátumát (ÉÉÉÉ-HH-NN): ")
            try:
                rental_date = date.fromisoformat(date_str)
                rental_company.rent_car(license_plate, rental_date)
            except ValueError:
                print("Hibás dátumformátum.")
        elif choice == "2":
            license_plate = input("Add meg a lemondandó bérlés rendszámát: ").upper()
            date_str = input("Add meg a lemondandó bérlés dátumát (ÉÉÉÉ-HH-NN): ")
            try:
                rental_date = date.fromisoformat(date_str)
                rental_company.cancel_rental(license_plate, rental_date)
            except ValueError:
                print("Hibás dátumformátum.")
        elif choice == "3":
            rental_company.list_rentals()
        elif choice == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")


if __name__ == "__main__":
    rental_company = setup_system()
    user_interface(rental_company)
