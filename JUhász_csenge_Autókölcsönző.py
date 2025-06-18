from abc import ABC, abstractmethod
from datetime import date
from typing import List, Optional


# -------- Auto absztrak osztály-----------# 

class Auto(ABC):
    def __init__(self,rendszam:str, tipus:str, berleti_dij:int):
      self.rendszam=rendszam  
      self.tipus=tipus
      self.berleti_dij= berleti_dij 
      
    @abstractmethod 
    def __str__(self):
        pass 
      
 # -------- Bérlő -----------#      
      
class Berlo:
    def __init__(self, nev):
        self.nev = nev

    def __str__(self):
        return self.nev
    
# ====== Személyautó osztály ======
class Szemelyauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, ulesek_szama: int, klima: bool):
        super().__init__(rendszam, tipus, berleti_dij)
        self.ulesek_szama = ulesek_szama
        self.klima = klima

    def __str__(self):
        klima_str = "van klíma" if self.klima else "nincs klíma"
        return (f"Személyautó - {self.rendszam}, Típus: {self.tipus}, Díj: {self.berleti_dij} Ft/nap, "
                f"Ülések: {self.ulesek_szama}, {klima_str}")


# ====== Teherautó osztály ======
class Teherauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, teherbiras: int, rakodoter_hossza: float):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras  # kg
        self.rakodoter_hossza = rakodoter_hossza  # méter

    def __str__(self):
        return (f"Teherautó - {self.rendszam}, Típus: {self.tipus}, Díj: {self.berleti_dij} Ft/nap, "
                f"Teherbírás: {self.teherbiras} kg, Rakodótér: {self.rakodoter_hossza} m")

# ====== Bérlés osztály ======
class Berles:
    def __init__(self, auto: Auto, datum: date):
        self.auto = auto
        self.datum = datum

    def __str__(self):
        return f"{self.auto.rendszam} - {self.auto.tipus} bérelve {self.datum}-én ({self.auto.berleti_dij} Ft)"



# ====== Autókölcsönző osztály ======
class Autokolcsonzo:
    def __init__(self, nev: str):
        self.nev = nev
        self.autok: List[Auto] = []
        self.berlesek: List[Berles] = []

    def auto_hozzaadasa(self, auto: Auto):
        self.autok.append(auto)

    def berles_hozzaadasa(self, berles: Berles):
        self.berlesek.append(berles)

    def auto_berelheto(self, rendszam: str, datum: date) -> Optional[Auto]:
        for auto in self.autok:
            if auto.rendszam == rendszam:
                # Ellenőrzés: van-e bérlés ugyanarra a napra
                if all(not (b.auto.rendszam == rendszam and b.datum == datum) for b in self.berlesek):
                    return auto
        return None

    def berel_auto(self, rendszam: str, datum: date):
        if datum < date.today():
            print("Nem lehet múltbeli dátumra bérlést rögzíteni.")
            return

        auto = self.auto_berelheto(rendszam, datum)
        if not auto:
            print("Ez az autó nem elérhető bérlésre a megadott napon.")
            return

        uj_berles = Berles(auto, datum)
        self.berlesek.append(uj_berles)
        print(f"Sikeresen bérelted az autót {auto.tipus} ({auto.rendszam}) {auto.berleti_dij} Ft-ért {datum}-én.")

    def berles_lemondasa(self, rendszam: str, datum: date):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self.berlesek.remove(berles)
                print(f"A(z) {rendszam} rendszámú autó {datum}-i bérlése lemondva.")
                return
        print("Nincs ilyen bérlés!")

    def listaz_berlesek(self):
        if not self.berlesek:
            print("Nincsenek aktív bérlések.")
        else:
            print("\nAktív bérlések:")
            for berles in sorted(self.berlesek, key=lambda b: (b.datum, b.auto.rendszam)):
                print(" -", berles)


# ====== Program inicializálása ======
def rendszer_elokeszitese() -> Autokolcsonzo:
    kolcsonzo = Autokolcsonzo("Autókölcsönző")
    
    print("--- Kezdeti bérlések ---")
    berlo1 = Berlo("Lakatos Nina")
    berlo2 = Berlo("Szoboszlai Csilla")
    berlo3 = Berlo("Kovács Kinga")
    berlo4 = Berlo("Berrei Enikő")
    berlo5 = Berlo("Turcsányi Lajos")

    kolcsonzo.auto_hozzaadasa(Szemelyauto("JKL-321", "Mazda 3", 8800, 5, True))
    kolcsonzo.auto_hozzaadasa(Szemelyauto("XYZ-654", "Volkswagen Golf", 9200, 5, False))
    kolcsonzo.auto_hozzaadasa(Teherauto("TRK-999", "Iveco Daily", 16000, 2000, 4.0))
    kolcsonzo.auto_hozzaadasa(Szemelyauto("AGDH-124", "Mazda 6", 8800, 5, True))
    kolcsonzo.auto_hozzaadasa(Szemelyauto("HJK-732", "Volkswagen PASSAT", 9200, 3, False))
    kolcsonzo.auto_hozzaadasa(Teherauto("OLP-286", "Ford Focus", 16000, 2000, 4.0))

    print("--- Új bérlések felvétele ---")
    kolcsonzo.berel_auto("JKL-321", date(2025, 6, 20))
    kolcsonzo.berel_auto("XYZ-654", date(2025, 6, 21))
    kolcsonzo.berel_auto("TRK-999", date(2025, 6, 22))
    kolcsonzo.berel_auto("XYZ-654", date(2025, 6, 21))  
    kolcsonzo.berel_auto("AAA-111", date(2025, 6, 24))  
    kolcsonzo.berel_auto("JKL-321", date(2024, 5, 15))  

    print("---------------------------")
    return kolcsonzo


# ====== Felhasználói interfész ======
def felhasznaloi_felulet(kolcsonzo: Autokolcsonzo):
    while True:
        print("\n--- Autókölcsönző rendszer ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Aktív bérlések listázása")
        print("4. Kilépés")
        valasztas = input("Válassz egy lehetőséget: ")

        if valasztas == "1":
            rendszam = input("Add meg a bérelni kívánt autó rendszámát: ").upper()
            datum_str = input("Add meg a bérlés dátumát (ÉÉÉÉ-HH-NN): ")
            try:
                datum = date.fromisoformat(datum_str)
                kolcsonzo.berel_auto(rendszam, datum)
            except ValueError:
                print("Hibás dátumformátum.")
        elif valasztas == "2":
            rendszam = input("Add meg a lemondandó bérlés rendszámát: ").upper()
            datum_str = input("Add meg a lemondandó bérlés dátumát (ÉÉÉÉ-HH-NN): ")
            try:
                datum = date.fromisoformat(datum_str)
                kolcsonzo.berles_lemondasa(rendszam, datum)
            except ValueError:
                print("Hibás dátumformátum.")
        elif valasztas == "3":
            kolcsonzo.listaz_berlesek()
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")


# ====== Program indítása ======
if __name__ == "__main__":
    kolcsonzo = rendszer_elokeszitese()
    felhasznaloi_felulet(kolcsonzo)
