from dataclasses import dataclass


@dataclass
class Personnage:
    _points_de_vie: int = 0
    _mort: bool = True

    def est_mort(self):
        return self._mort

    def tuer(self):
        self._points_de_vie = 0
