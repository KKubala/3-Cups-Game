from ekran import *
import time


def wybierz(font, ekran, ts, podczerwien, ilosc):
    '''
    Funkcja  pozwala użytkownikowi dokonywać wyboru levelu lub kubków.
    Wyświetla tryb i aktualny wybór na ekranie. Dmyślnym wyborem jest 1.
    Zmiany wyboru można dokonać za pomocą pilota.
    Zatwierdzamy wciśniętym czujnikiem dotyku.
    (font, Display, TouchSensor, InfraredSensor, int) -> int

    Argumenty:
    font - font, którym wyświetlimy treści na ekranie
    ekran - obiekt typu Display, na którym wyświetlamy treści
    ts - obiekt typu TouchSensor, dzięki niemu zatwierdzamy wybór
    podczerwien. obiekt typu InfraredSensor, za jego pomocą obsługujemy
    pilota, któym możemy zmieniać wybór
    ilosc - ilość dostępnych wyborów. int[3, 4]

    Wynik:
    Funkcja zwraca numer wybrany przez użytkownika (levelu lub kubka)
    '''
    wybor = 1
    tryb = "LEVEL" if ilosc == 4 else "CUP"
    wyswietlanie(font, ekran, tryb, wybor)

    while (not ts.is_pressed):
        if(podczerwien.top_left(channel=1) and wybor < ilosc):
            wybor += 1
            wyswietlanie(font, ekran, tryb, wybor)
            time.sleep(0.2)
        if(podczerwien.bottom_left(channel=1) and wybor > 1):
            wybor -= 1
            wyswietlanie(font, ekran, tryb, wybor)
            time.sleep(0.2)
    time.sleep(0.3)
    return wybor


def tak_nie(font, ekran, ts, podczerwien, tryb):
    '''
    Funkcja  pozwala użytkownikowi dokonywać wyborów typu Tak/Nie
    Wyświetla tryb i aktualny wybór na ekranie. Dmyślnym wyborem jest "Yes".
    Zmiany wyboru można dokonać za pomocą pilota.
    Zatwierdzamy go wciśniętym czujnikiem dotyku.
    (font, Display, TouchSensor, InfraredSensor, int) -> Bool

    Argumenty:
    font - font, którym wyświetlimy treści na ekranie
    ekran - obiekt typu Display, na którym wyświetlamy treści
    ts - obiekt typu TouchSensor, dzięki niemu zatwierdzamy wybór
    podczerwien. obiekt typu InfraredSensor, za jego pomocą obsługujemy
    pilota, któym możemy zmieniać wybór
    tryb - tryb wyboru.
    Istnieją dwa możliwe tryby: "Want Guess?" i "Play again?"

    Wynik:
    Funkcja zwraca Bool wybrany przez użytkownika.
    '''
    opcje = ["Yes", "No"]
    wybor = 0
    wyswietlanie(font, ekran, tryb, opcje[0])

    while (not ts.is_pressed):
        if(podczerwien.top_left(channel=1) or
           podczerwien.bottom_left(channel=1)):
            wybor = (wybor + 1) % 2
            wyswietlanie(font, ekran, tryb, opcje[wybor])
            time.sleep(0.2)
    time.sleep(0.5)
    return True if wybor == 0 else False
