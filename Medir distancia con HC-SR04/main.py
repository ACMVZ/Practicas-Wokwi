from machine import Pin, time_pulse_us
import time

time.sleep(0.1) # Wait for USB to become ready

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def get_distance():
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(10)
    trigger.low()
    duration = time_pulse_us(echo, 1)
    distance = duration / 58
    return distance

while True:
    print("Distancia:", get_distance(), "cm")
    time.sleep(1)
