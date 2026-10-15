class registro_voit:
    def __init__(self):
        self.voti = []

    def aggiungi_voto(self, voto: int):
        if 0 < voto <= 10:
            self.voti.append(voto)
        else:
            raise ValueError("Il voto deve essere compreso tra 0 e 10")

    def risultati(self):
        