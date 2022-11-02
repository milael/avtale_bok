import datetime
from datetime import datetime, timedelta


class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet

    def __str__(self):
        print(f'Avtalen: {self.tittel} foregår kl. {self.starttidspunkt}'
              f'Sted: {self.sted} Varighet: {self.varighet}')

# det er en test











