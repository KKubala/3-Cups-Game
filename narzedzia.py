from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_B, OUTPUT_C, OUTPUT_A
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.sound import Sound
from ev3dev2.display import Display
import ev3dev2.fonts as fonts

'''
sound - obsługuje dźwięk robota
ts - czujnik dotyku
podczerwień - czujnik podczerwieni. Obsuguje pilota.
silnikB - duży silnik w porcie B.
silnikC - duży silnik w porcie C.
manipulator - średni silnik w porcie A
ekran - obiekt obsłuujący treści wyświetlane na ekranie robota.
font - font używany do wyświetlania treści.
'''
sound = Sound()
ts = TouchSensor(INPUT_1)
podczerwien = InfraredSensor(INPUT_4)
silnikB = LargeMotor(OUTPUT_B)
silnikC = LargeMotor(OUTPUT_C)
manipulator = MediumMotor(OUTPUT_A)
ekran = Display()
font = fonts.load('luBS24')
