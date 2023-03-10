import random
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


autot = []

for i in range(10):
    auto = Auto("ABC-"+str(i+1), random.randint(100, 200))
    autot.append(auto)
continueLoop = True
while (continueLoop):

    for i in autot:
        i.kiihdyta(random.randint(-10, 15))
        i.kulje(1)
        if i.getKuljettuMatka() >= 8000:
            continueLoop = False
            break
        print(i.getKuljettuMatka())




for count, i in enumerate(autot):
    print(
        f"auton {count+1} nopeus on {i.getNopeus()} km/h, kuljettu matka on {i.getKuljettuMatka()}km, huippunopeus on {i.getHuippunopeus()} km/h ja "
        f"rekisteritunnus on {i.getRekisteritunnus()}")




