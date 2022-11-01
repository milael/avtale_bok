import datetime
from datetime import datetime

class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet
    def __str__(self):
        print(f'Du har {self.tittel} på {self.sted} fra {self.starttidspunkt} til {self.starttidspunkt + self.varighet}')