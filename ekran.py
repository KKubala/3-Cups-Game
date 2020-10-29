def wyswietlanie(font, ekran, tryb, wybor):
    '''
    Funkcja wyświetla treści na ekranie.
    Najpierw czyści ekran z poprzedniej treści. Następnie wyświetla
    tryb w górnej części ekranu oraz wybraną opcję po środku.
    Na koniec aktualizuje ekran.

    Argumenty:
    font - font, którego używamy do wyświetlania
    ekran - obkekt klasy Display, na którym wyświetlamy teści.
    tryb - napis informuje użytkownika co ma do wyboru.
    Istnieją cztery tryby ["Level", "Cup", "Want Guess?", "Play again?"]
    wybor - opcja wybierana przez użytkownika. [1, 2, 3, 4, "YES", "NO"]
    '''
    ekran.clear()
    ekran.draw.text((10, 10), tryb, font)
    ekran.draw.text((80, 60), str(wybor), font)
    ekran.update()
