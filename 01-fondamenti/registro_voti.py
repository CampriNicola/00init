class registro_voit:
    def __init__(self):
        self.voti = []

    def aggiungi_voto(self, voto: int):
        if 0 < voto <= 10:
            self.voti.append(voto)
        else:
            raise ValueError("Il voto deve essere compreso tra 0 e 10")

    def risultati(self):
        result = ""
        for voto in self.voti:
            if voto >= 6:
                resut += "sufficiente, "
            else:
                result += "insufficente, "

        return result

    def media(self):
        totSum = 0
        count = len(self.voti)

        for voto in self.voti:
            totSum += voto

        return totSum / count