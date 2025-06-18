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
    
# ====== Teherautó osztály ====== # 

class Teherauto(Auto):
         def __str__(self):
             return f"Teherautó - {self.rendszam}, Típus: {self.tipus}, Bérletid díj: {self.berleti_dij} Ft/nap"