import random  
from datetime import datetime  


class Film:
    def __init__(self, tytul, rok_wydania, gatunek):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = 0 

    def play(self):
        
        self.liczba_odtworzen += 1

    def __str__(self):
        
        return f"{self.tytul} ({self.rok_wydania})"


class Serial(Film):
    def __init__(self, tytul, rok_wydania, gatunek, numer_odcinka, numer_sezonu):
        super().__init__(tytul, rok_wydania, gatunek)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def __str__(self):
        
        return f"{self.tytul} S{self.numer_sezonu:02}E{self.numer_odcinka:02}"


biblioteka = []


def get_movies(biblioteka):
   
    return sorted([item for item in biblioteka if isinstance(item, Film) and not isinstance(item, Serial)], key=lambda x: x.tytul)

def get_series(biblioteka):
    
    return sorted([item for item in biblioteka if isinstance(item, Serial)], key=lambda x: x.tytul)

def search(biblioteka, tytul):
    
    for item in biblioteka:
        if item.tytul.lower() == tytul.lower():
            return item
    return None  

def generate_views(biblioteka):
    
    item = random.choice(biblioteka)
    
    item.liczba_odtworzen += random.randint(1, 100)

def run_generate_views(biblioteka, times=10):
    
    for _ in range(times):
        generate_views(biblioteka)

def top_titles(biblioteka, n=3):
    
    return sorted(biblioteka, key=lambda x: x.liczba_odtworzen, reverse=True)[:n]

def wyswietl_najpopularniejsze(biblioteka):
    
    dzisiaj = datetime.now().strftime("%d.%m.%Y")
    print(f"Najpopularniejsze filmy i seriale dnia {dzisiaj}:")
    
    
    top = top_titles(biblioteka, 3)
    for item in top:
        print(f"{item} - {item.liczba_odtworzen} odtworzeń")


biblioteka.append(Film("Pulp Fiction", 1994, "Crime"))
biblioteka.append(Film("The Godfather", 1972, "Crime"))
biblioteka.append(Serial("The Simpsons", 1989, "Comedy", 5, 1))
biblioteka.append(Serial("Breaking Bad", 2008, "Drama", 1, 1))
biblioteka.append(Serial("Friends", 1994, "Comedy", 10, 1))


print("Biblioteka filmów i seriali")


run_generate_views(biblioteka)


wyswietl_najpopularniejsze(biblioteka)
