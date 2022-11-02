import datetime
from datetime import datetime, timedelta

''' Milael:
    d) Lag en klasse for en avtale. En avtale skal minimum ha:
        a. En tittel som sier hva denne avtalen er (streng)
        b. Et sted (streng)
        c. Et starttidspunkt (datetime objekt, se hint nederst)
        d. En varighet i minutter (int)'''

class Appointment:
    def __init__(self, titel, place, start_time, duration):
        self.titel = titel
        self.place = place
        self.start_time = start_time
        self.duration = duration

    ''' Milael:
        e) Lag en __str__ metode for avtaler som returnerer en streng 
        som kan skrives ut med en print-setning slik at du får skrevet ut avtalen 
        med alle egenskapene til avtalen på et leselig format for brukeren.'''

    def __str__(self):
        print(f'Avtalen: {self.titel} foregår kl. {self.start_time}'
              f'Sted: {self.place} Varighet: {self.duration}')



''' Milael:
    f) Lag en funksjon som lar brukeren skrive inn en ny avtale. 
    Funksjonen skal bruke input-funksjonen til å lese inn egenskapene til avtalen 
    og skal sjekke at det brukeren skriver er gyldig, for eksempel at varighet er et tall. 
    Funksjonen skal returnere et avtale-objekt'''

''' Mehdi: 
    g) Lag en funksjon som skriver ut ei liste med avtaler til skjermen. 
    Funksjonen skal minimum skrive ut indeksen til avtalen i lista og tittel til avtalen. 
    Den kan alternativt skrive ut indeksen til avtalen 
    og så hele avtalen som definert i __str__ metoden. 
    Funksjonen skal ha en frivillig parameter «overskrift» 
    som skal være en overskrift som funksjonen skriver ut før avtalene i lista. 
    Funksjonen skal inkludere indeksen til hver avtale i utskriften. '''

appointment_list = []


def print_appointment():
    for i in appointment_list:
        print(appointment_list[i])


print_appointment()


''' Mehdi:
    h) Lag en funksjon som lagrer ei liste med avtaler til ei tekstfil. 
    Tenk over hva som vil være et fornuftig format for ei slik tekstfil.'''










