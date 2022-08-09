from Animal import Animal


class Seahorse(Animal):

    def __int__(self, name, colour, goodSwimmer, luckyFin):
        Animal.__init__("Seahorse", name, colour)
        self.goodSwimmer = goodSwimmer
        self.luckyFin = luckyFin


