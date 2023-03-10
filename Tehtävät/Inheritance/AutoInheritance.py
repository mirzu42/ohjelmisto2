class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus=huippunopeus
        self.nopeus=0
        self.KuljettuMatka=0
    def getNopeus(self):
        return self.nopeus
    def getRekisteritunnus(self):
        return self.rekisteritunnus
    def getHuippunopeus(self):
        return self.huippunopeus
    def getKuljettuMatka(self):
        return int(self.KuljettuMatka)

    def kiihdyta(self, nopeus):
        if self.nopeus + nopeus>=self.getHuippunopeus():
            self.nopeus=self.getHuippunopeus()
        elif self.nopeus + nopeus<0:
            self.nopeus = 0
        else:
            self.nopeus += nopeus

    def kulje(self, tuntimaara):
        self.KuljettuMatka+=tuntimaara*self.getNopeus()

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, kapasiteettiKWH):
        self.kapasiteettiKWH = kapasiteettiKWH #ei käytetä mihinkään?
        super().__init__(rekisteritunnus, huippunopeus)
class PolttomoottoriAuto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankinKokoL):
        self.tankinKoko = tankinKokoL #ei käytetä mihinkään?
        super().__init__(rekisteritunnus, huippunopeus)

class main():
    ekaAuto = Sahkoauto("ABC-123", 190, 65)
    tokaAuto = PolttomoottoriAuto("ABC-321", 220, 40)
    ekaAuto.kiihdyta(100)
    ekaAuto.kulje(3)
    tokaAuto.kiihdyta(169)
    tokaAuto.kulje(3)
    print(f"Sähköauton nopeus: {ekaAuto.getNopeus()}, rekisteritunnus: {ekaAuto.getRekisteritunnus()}, huippunopeus: {ekaAuto.getHuippunopeus()}, "
          f"kuljettu matka: {ekaAuto.getKuljettuMatka()}")
    print(
        f"Polttomoottoriauton nopeus: {tokaAuto.getNopeus()}, rekisteritunnus: {tokaAuto.getRekisteritunnus()}, huippunopeus: {tokaAuto.getHuippunopeus()}, "
        f"kuljettu matka: {tokaAuto.getKuljettuMatka()}")