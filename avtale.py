import datetime
from datetime import datetime, timedelta

''' d) Lag en klasse for en avtale. En avtale skal minimum ha:
        a. En tittel som sier hva denne avtalen er (streng)
        b. Et sted (streng)
        c. Et starttidspunkt (datetime objekt, se hint nederst)
        d. En varighet i minutter (int)'''

class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet

    ''' e) Lag en __str__ metode for avtaler som returnerer en streng 
        som kan skrives ut med en print-setning slik at du får skrevet ut avtalen 
        med alle egenskapene til avtalen på et leselig format for brukeren.'''

    def __str__(self):
        print(f'Avtalen: {self.tittel} foregår kl. {self.starttidspunkt}'
              f'Sted: {self.sted} Varighet: {self.varighet}')













