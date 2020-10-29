from kulka import *
import random
import time


def zamieszaj(silnikB, silnikC, poziom):
    '''
    Funkcja miesza kubkami obracając silnikami.
    Ilość i szybkość obrotów jest losowa ale zależna od wybranego poziomu.
    (LargeMotor, LargeMotor, int) -> int

    Argumenty:
    silnikB - Obiekt klasy LargeMotor. Jego obrót zamieia kubek 1 i 2
    silnikc - Obiekt klasy LargeMotor. Zamienia kubek 2 z 3
    poziom - wybrany przez użytkownika poziom trudności.
    Decyduje o szybkości i ilości obrotów. int[1,2,3,4]

    Wynik:
    Wynikiem funkcji jest numer kubka pod którym znajduje się kulka. int[1,2,3]
    '''
    kulka = 2
    for i in range(random.randint(10*poziom, 10*(poziom+1))):
        strona = random.randint(1, 4)
        if strona == 1:
            kulka = przekrec(silnikB, "B", poziom, 230, -50, kulka)
        elif strona == 2:
            kulka = przekrec(silnikB, "B", poziom, -230, 50, kulka)
        elif strona == 3:
            kulka = przekrec(silnikC, "C", poziom, 230, -50, kulka)
        elif strona == 4:
            kulka = przekrec(silnikC, "C", poziom, -230, 50, kulka)
    return kulka


def przekrec(silnik, strona, poziom, stopien, powrot, kulka):
    '''
    Funkcja obraca wybranym silnikiem najpierw o 230* a następnie o 50*
    w drugą stronę. Dzięki temu ostatecznie pozycja mieszadła zmienia się
    o równo 180*, a kubek ustawiają się w wyśrodkowanej pozycji.
    Następnie uruchamia monit_kulki aby zaktualizować pozycję kubka
    pod którym znajduje się kulka.
    (LargeMotor, str, int, int, int, int) -> int

    Argumenty:
    silnik - obiekt klasy LargeMotor, którym będziemy obracać.
    silnikB lub silnikC
    strona - nazwa silnika. "B" lub "C"
    poziom - wybrany poziom trudności, zależy od niego prękość obrotu.
    int[1,2,3,4]
    stopien - stopień o który obracamy silnik.
    int[230, -230]
    powrot - o ile musi wrócić silnik, aby finalnie wykonał 180.
    int[50, -50]
    kulka - pozycja na której znajdowała się kulka przed obrotem.
    int[1,2,3]

    Wynik:
    Funkcja zwraca numer kubka, pod którym znajduje się kulka po obrocie.
    int[1,2,3]
    '''
    silnik.on_for_degrees(speed=(poziom*10), degrees=stopien)
    silnik.on_for_degrees(speed=(poziom*10), degrees=powrot)
    kulka = monit_kulki(strona, kulka)
    time.sleep(0.5)
    return kulka


def sprawdz(sound, manipulator, silnikB, silnikC, wybor, kulka):
    '''
    Funkcja sprawdz sprawdza czy wybrany przez użtkownika kubek zawiera kulkę.
    W tym celu zamienia kubki w taki sposób aby wybrany kubek znajdował się
    na środkowej pozycji. I podnosi go za pomocą manipulatora.
    Jeśli kulka znajduje się pod wybranym kubkiem Wydaje dzwięk "Congratulatio"
    wpp. wydaje komunikat dzwięk "Sorry, you are wrong!".
    Następnie odstawia kubek.
    (Sound, MediumMotor, LargeMotor, LargeMotor, int, int) -> (Bool, int)

    Argumenty:
    sound - obiekt klasy Sound. Obsługuje dzwięk i wydaje komunikaty.
    manipulator - obiekt klasy MediumMotor - obsługuje dzwignie podnoszącą i
    opuszczającą kubek na środkowej pozycji.
    silnikB - obiekt klasy LargeMotor. Silnik zamieniający kubek 1 i 2
    silnikC - obiekt klasy LargeMotor. Silnik zamieniający kubek 2 i 3
    wybor - wybrany przez użytkownika kubek, jako ten zawierający kulkę.
    int[1,2,3]
    kulka - rzeczywista pozycja kulki. int[1,2,3]

    Wynik:
    Funkcja zwaca parę (Bool, kulka)
    Bool - informuje czy użytkownik odgadł poprawnie pozcję kulki.
    kulka - numer kubka pod którym znajduje się po wykonaniu funkcji.
    '''
    if wybor == 1:
        kulka = przekrec(silnikB, "B", 2, 230, -50, kulka)
    elif wybor == 3:
        kulka = przekrec(silnikC, "C", 2, 230, -50, kulka)
    manipulator.on_for_degrees(speed=10, degrees=220)
    if kulka == 2:
        sound.speak("Congratulation!")
        manipulator.on_for_degrees(speed=10, degrees=-220)
        return (True, kulka)
    else:
        sound.speak("Sorry, you are wrong!")
        manipulator.on_for_degrees(speed=10, degrees=-220)
        return (False, kulka)
