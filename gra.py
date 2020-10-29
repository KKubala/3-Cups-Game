#!/usr/bin/env python3
from wybor import *
from narzedzia import *
from silniki import zamieszaj, sprawdz

# Main
'''
Główny plik gry.
Odpowiada za całą rozgrywkę.

gra - decyduje o tym czy program powinien działać czy się zakończyć.
Początkowo jest równa True, zmienia się na False jeśli użytkownik zdecyduje,
że nie chce grać ponownie.

poziom - wybrany przez użytkownika poziom trudności gry [1,2,3,4]

kulka - numer kubka pod którym znajduje się kulka po zakończeniu mieszania.

zagadka - zmienna Bool informująca czy użytkonik odgadł pozucję kulki.

wybor - kubek wybrany przez użytkownika jako ten zawierający kulkę.

Opis rozgrywki.
Najpierw użytkownik ma możliwość wyboru jednego z czterech poziomów trudnośći.
Poziom ten odpowiada za ilość i szybkość obrotu silników.
Wszelkich wyborów możemy dokonywać za pomocą pilota z zestawu.
Następnie zatwierdza swój wybór wciskająć czujnik dotyku.
Program przystępuje do mieszania kubków. Zależnie od wybranego poziomu nastąpi
to od 10 do 50 razy. Z prędkością od 10% do 40% mocy silnika.
Kiedy mieszanie się zakończy gracz zostanie poproszony o wybór kubka pod
którym, jego zdaniem znajduje się kulka. Jeśli jego wybór był poprawny, robot
pogratuluje graczowi i zaproponuje mu zagranie pozownie. Jeśli wybór był
niepoprawny, możemy zdecydować czy chcemy zgadywać jeszcze raz.
Jeśli nie chcemy zgadywać dalej lub zgadniemy ponownie, mamy możliwość zagrania
jeszcze raz.
Gdy użytkownik zdecyduje się nie grać ponownie program wyłączy się.
'''
gra = True

while gra:
    poziom = wybierz(font, ekran, ts, podczerwien, 4)
    kulka = zamieszaj(silnikB, silnikC, poziom)
    zagadka = False
    while not zagadka:
        if (not tak_nie(font, ekran, ts, podczerwien, "Want Guess?")):
            break
        wybor = wybierz(font, ekran, ts, podczerwien, 3)
        [zagadka, kulka] = sprawdz(sound, manipulator, silnikB,
                                   silnikC, wybor, kulka)
    gra = tak_nie(font, ekran, ts, podczerwien, "Play again?")
