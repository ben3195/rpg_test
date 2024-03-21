from dataclasses import dataclass
from random import randint

@dataclass
class Personnage:
    _points_de_vie: int = 100
    _mort: bool = False

    def est_mort(self):
        return self._mort

    def get_point_de_vie(self):
        return self._points_de_vie

    def subit_attaque(self, point_perdu: int):
        self._points_de_vie -= point_perdu

    def attaque(self, other: 'Personnage', puissance: int):
        other.subit_attaque(puissance)

    def tuer(self):
        self._points_de_vie = 0
        self._mort = True

