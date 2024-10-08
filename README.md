Biblioteka Filmów i Seriali

Opis projektu-
Ten projekt to prosty system zarządzania biblioteką filmów i seriali, zbudowany w oparciu o zasady programowania obiektowego. Program umożliwia:

        Przechowywanie informacji o filmach i serialach,
        Odtwarzanie treści, które zwiększa liczbę odtworzeń,
        Wyszukiwanie filmów lub seriali po tytule,
        Losowe generowanie odtworzeń dla filmów i seriali,
        Wyświetlanie najpopularniejszych tytułów na podstawie liczby odtworzeń.

        
Funkcjonalności-
  Filmy i seriale:

      Filmy i seriale mają takie atrybuty jak tytuł, rok wydania, gatunek, liczba odtworzeń.
      Serial dodatkowo posiada numer odcinka i numer sezonu.
      Każdy film i serial posiada metodę play(), która zwiększa liczbę odtworzeń o 1.
      Wyświetlenie serialu prezentuje jego tytuł w formacie Tytuł SXXEYY (gdzie XX to sezon, a YY to odcinek).
      Wyświetlenie filmu prezentuje jego tytuł w formacie Tytuł (Rok).
  Generowanie odtworzeń:

      Program posiada funkcję generate_views(), która losowo wybiera film lub serial z biblioteki i zwiększa jego liczbę odtworzeń o losową wartość (od 1 do 100).
      Funkcja run_generate_views() pozwala na wielokrotne uruchomienie generate_views().
 Najpopularniejsze tytuły:

      Funkcja top_titles() zwraca najpopularniejsze tytuły na podstawie liczby odtworzeń.
      Program wyświetla najpopularniejsze filmy i seriale dnia z aktualną datą.
      
Wymagania-
        Python 3.x
        Biblioteka standardowa Pythona:
        random (do losowego generowania odtworzeń)
        datetime (do uzyskania bieżącej daty)
