class Libro:
    #def = funzione __init__ = costruttore
    #senza self avremo soltanto un oggetto
    def __init__(self, titolo: str, autore: str, anno: int, editore: str, pagine: int):
        self.titolo = titolo # self.titolo è una property di libro
        self.autore = autore
        self.anno = anno
        self.editore = editore
        self.pagine = pagine

    def reading_time(self) -> str: #metodo senza parametri  -> str = tipo di ritorno str
        if self.pagine < 100:
            return "1 ora"
        if self.pagine <= 2:
            return "2 ore"
        return "più di 2 ore"

    #ToString 
    def __str__(self):
        # f è il $ in C# interpolazione
        return f"{self.titolo} - {self.autore} ({self.anno}), {self.pagine} pagine"

class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        self.libri = [] #creazione di una lista generica

    def aggiungi_libro(self, libro: Libro) -> None:
        self.libro.append(libro)

    def cerca_per_titolo(self, testo: str) -> Libro:
        testo = testo.lower()

        for libro in self.libri:
            if testo in libro.titolo.lower():
                return libro
        return None

    def cerca_per_autore(self, autore: str):
        autore = autore.lower()

        libri_autore = []
        for libro in self.libri:
            if autore in libro.autore.lower():
                libri_autore.append(libro)

        return libri_autore

    def conta_liberi(self):
        return len(self.libri) # .lenght n C#

class Prestito:
    def __init__(self, libro, utente):
        self.libro = libro
        self.utente = utente

    def __str__(self):
        return f"{self.utente} ha preso in prestito: {self.libro.titolo}"

#richiamo del main / punto di partenza di questo file python
if __name__ == "__main__":
    libro1 = Libro("", "", 1000, "", 200)

    biblioteca = Biblioteca("Biblioteca Scolastica")

    biblioteca.aggiungi_libro(Libro("Il nome della rosa", "Umberto Eco", 1980, "Bompiani", 568))
    biblioteca.aggiungi_libro(Libro("Se questo è un uomo", "Primo Levi", 1947, "Einaudi", 180))

    print(f"Numero libri: {biblioteca.conta_liberi()}")
    print("Risultati ricerca per autore 'eco': ")
    for libro in biblioteca.cerca_per_autore("eco"):
        print(f"{libro.titolo}: tempo lettura {libro.reading_time()}")
   