from time import sleep

from machine import PWM, Pin

buzzer = PWM(Pin(25))


def beep(freq=1000, duration=0.5):
    buzzer.freq(freq)
    buzzer.duty(512)
    sleep(duration)
    buzzer.duty(0)
