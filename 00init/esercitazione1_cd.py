class Brano:
    def __init__(self, titolo, autore, durata):
        self.titolo = titolo
        self.autore = autore
        self.durata = durata

    def __str__(self): 
        return f"{self.titolo} {self.durata} - {self.autore}"

    def shortSong(self, value: int) -> bool:
        if value > self.durata: 
            return True
        else:
            return False


class Cd:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.brani = []
        self.durata = 0

    def __str__(self):
        numeroBrani = len(self.brani)
        return f"{self.titolo} numero brani: {numeroBrani} durata total: {self.durata} - {self.autore}"

    def aggiungiBrano(self, brano: Brano) -> None:
        self.brani.append(brano)
        self.durata += brano.durata


if __name__ == "__main__":
    brano1 = Brano("titolo1", "autorex", 2)
    brano2 = Brano("titolo2", "autorex", 3)

    print(f"{brano1.shortSong(4)}")

    nuovo_cd = Cd("album", "autoreX")
    nuovo_cd.aggiungiBrano(brano1)
    nuovo_cd.aggiungiBrano(brano2)

    print(nuovo_cd)
