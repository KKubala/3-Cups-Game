class LargeMotor:
    def __init__(self, port):
        self.port = port

    def on_for_degrees(self, speed=0, degrees=0):
        pass


class InfraredSensor:
    def __init__(self, port):
        self.port = port

    def top_left(self, chanel=1):
        self.chanel = chanel
        pass

    def bottom_left(self, chanel=1):
        self.chanel = chanel
        pass


class MediumMotor:
    def __init__(self, port):
        self.port = port

    def on_for_degrees(self, speed=0, degrees=0):
        pass


class Sound:
    def __init__(self):
        pass

    def speak(self, tekst):
        pass


class Draw:
    def text(self, miejsce, tekst, font):
        pass


class Display:
    def __init__(self):
        self.draw = Draw()
        pass

    def clear(self):
        pass

    def update(self):
        pass


class TouchSensor:
    def __init__(self, input="1"):
        self.input = input
        self.iteration = 0
        self.odpowiedzi = [False]

    def ustaw_odpowiedzi(self, odpowiedzi):
        self.odpowiedzi = odpowiedzi
        self.iteration = 0

    @property
    def is_pressed(self):
        try:
            odpowiedz = self.odpowiedzi[self.iteration]
        except IndexError:
            raise Exception(f'Poza zakresem tablicy')
        self.iteration += 1
        return odpowiedz


OUTPUT_B = "B"
OUTPUT_C = "C"
OUTPUT_A = "A"
INPUT_4 = "4"
INPUT_1 = "1"
ts = TouchSensor(INPUT_1)
podczerwien = InfraredSensor(INPUT_4)
ekran = Display()
manipulator = MediumMotor(OUTPUT_A)
silnikB = LargeMotor(OUTPUT_B)
silnikC = LargeMotor(OUTPUT_C)
sound = Sound()
font = "font"
