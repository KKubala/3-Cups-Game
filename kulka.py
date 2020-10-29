def monit_kulki(silnik, kulka):
    '''
    Funkcja monit_kulki monitoruje pozycję kulki
    (stirng, int) -> int

    Argumenty:
    silnik - nazwa silnika, który zostanie obrócony, w praktyce może być to
    tylko "B" lub "B"
    kulka - pozycja kulki przed obróceniem silnika czyli int [1, 2, 3]

    Wynik:
    Funkcja zwraca pozycję kulki po obrocie silnika czyli int [1, 2, 3]
    '''
    if (silnik == "B" and kulka == 2) or (silnik == "C" and kulka == 1):
        return 1
    elif (silnik == "B" and kulka == 1) or (silnik == "C" and kulka == 3):
        return 2
    elif (silnik == "B" and kulka == 3) or (silnik == "C" and kulka == 2):
        return 3
