#Tehtävät 1, 2 ja 3
class Hissi():
    nykyinenKerros = 0

    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinenKerros=alin



    def siirry_kerrokseen(self, kerros):
        if(self.nykyinenKerros<self.ylin and (kerros<=self.ylin)):
            for i in range (kerros - self.nykyinenKerros):
                self.kerros_ylos()
        if (self.nykyinenKerros>self.alin and kerros>=self.alin):
            for x in range(self.nykyinenKerros - kerros):
                self.kerros_alas()
        return
    def kerros_ylos(self):
        if (self.nykyinenKerros<self.ylin):
            self.nykyinenKerros+=1
            print(f"Hissi on nyt kerroksessa {self.nykyinenKerros}")
        return
    def kerros_alas(self):
        if (self.nykyinenKerros>self.alin):
            self.nykyinenKerros-=1
            print(f"Hissi on nyt kerroksessa {self.nykyinenKerros}")
        return

class Talo():

    def __init__(self, alinKerros, ylinkerros, hissienLukumaara):
        self.hissit = []
        self.alin = alinKerros
        self.ylin = ylinkerros
        self.hissienLukumaara = hissienLukumaara
        for i in range(hissienLukumaara):
            h = Hissi(alinKerros, ylinkerros)
            self.hissit.append(h)
       # for count, i in enumerate(hissit):
        #    print(f"Talossa on {count+1} hissiä")

    def getHissit(self):
        return self.hissienLukumaara
    def getAlin(self):
        return self.alin
    def getYlin(self):
        return self.ylin
    def aja_hissia(self, hissinNumero, kerros):
        return self.hissit[hissinNumero-1].siirry_kerrokseen(kerros)
    def palohalytys(self):
        for i in self.hissit:
            i.siirry_kerrokseen((self.alin))


class main():
    talo = Talo(1, 8, 6)
    talo.aja_hissia(1, 8)
    talo.aja_hissia(4, 2)
    talo.aja_hissia(6, 7)
    talo.aja_hissia(1, 4)
    talo.palohalytys()



