class Studente:
    def __init__(self, nome, cognome, eta, citta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.citta = citta

    def __str__(self):
        return f"{self.nome} {self.cognome} - Eta: {self.eta} - Citta: {self.citta}"

    def classificazione(self):
        if 14 <= self.eta <= 16:
            return "Biennio"
        elif 17 <= self.eta <= 19:
            "Triennio"
        else: 
            "altro"

class Scuola:
    def __init__(self, nome):
        self.nome = nome
        self.studenti = []

    def aggiungi_studente(self, studente):
        self.studenti.append(studente)

    def ricerca_cognome(self, cognome: str):
        cognome = cognome.lower()

        result = []
        for studente in self.studenti:
            if studente.cognome.lower() == cognome:
                result.append(studente)

        return result
