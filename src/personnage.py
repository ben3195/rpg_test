from dataclasses import dataclass


@dataclass
class Personnage:
    _points_de_vie: int = 100
    _mort: bool = False

    def est_mort(self):
        return self._mort

    def tuer(self):
        self._points_de_vie = 0
        self._mort = True

