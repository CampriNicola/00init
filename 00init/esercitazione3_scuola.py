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

    def ricerca_eta(self, eta):
        result = []
        for studente in self.studenti:
            if studente.eta == eta:
                result.append(studente)

        return result

    def conteggio_studenti(self):
        return len(self.studenti)

if __name__ == "__main__":
    studente1 = Studente("Carlo", "Rossi", 14, "Cesena")
    studente2 = Studente("Arianna", "Esposito", 20, "Cesena")
    studente3 = Studente("Alberto", "Rossi", 18, "Forli")

    scuola = Scuola("Pascal2")
    scuola.aggiungi_studente(studente1)
    scuola.aggiungi_studente(studente2)
    scuola.aggiungi_studente(studente3)

    print(f"Numero studenti: {scuola.conteggio_studenti()}")

    print("Ricerca per cognome Rossi")
    for studente in scuola.ricerca_cognome("Rossi"):
        print(f"stud) {studente}")

    print("Ricerca per eta 14")
    for studente in scuola.ricerca_eta(14):
        print(f"stud) {studente}")

