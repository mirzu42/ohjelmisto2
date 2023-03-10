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

class Kilpailu():
    def __init__(self, nimi, pituuskm, osallistujat):
        self.nimi = nimi
        self.pituuskm = pituuskm
        self.osallistujat = osallistujat

    def tunti_kuluu(self):
        for i in self.osallistujat:
            i.kiihdyta(random.randint(-10, 15))
            i.kulje(1)
    def tulosta_tilanne(self):
        for count, i in enumerate(self.osallistujat):
            print(
                f"auton {count + 1} nopeus on {i.getNopeus()} km/h, kuljettu matka on {i.getKuljettuMatka()}km, huippunopeus on {i.getHuippunopeus()} km/h ja "
                f"rekisteritunnus on {i.getRekisteritunnus()}")

    def kilpailu_ohi(self):
        for i in self.osallistujat:
            if (i.getKuljettuMatka() >= self.pituuskm):
                return True
            else:
                continue


class main():
    autot = []
    for i in range(10):
        auto = Auto("ABC-" + str(i + 1), random.randint(100, 200))
        autot.append(auto)

    k = Kilpailu("Suuri romuralli", 8000, autot)
    tunnit = 0


    while (True):
        k.tunti_kuluu()

        tunnit += 1
        if k.kilpailu_ohi():
            k.tulosta_tilanne()
            break


        if (tunnit % 10 == 0):
            print("tunti: " + str(tunnit))
            k.tulosta_tilanne()














