class Julkaisu():
    def __init__(self, nimi):
      self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)
    def tulostaTiedot(self):
        print(f" Nimi: {self.nimi}\n kirjoittaja: {self.kirjoittaja}\n sivumäärä: {self.sivumaara}")
class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulostaTiedot(self):
        print(f" Nimi: {self.nimi}\n päätoimittaja: {self.paatoimittaja}")


class main():
    kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
    lehti =Lehti("Aku Ankka", "Aki Hyyppä")
    kirja.tulostaTiedot()
    lehti.tulostaTiedot()