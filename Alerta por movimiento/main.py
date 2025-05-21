from machine import Pin
import time

time.sleep(0.1) # Wait for USB to become ready

pir = Pin(13, Pin.IN)
buzzer = Pin(12, Pin.OUT)
led = Pin(11, Pin.OUT)

while True:
    if pir.value():
        buzzer.on()
        led.on()
        print("¡WII! ¡WOO! ¡WII! ¡WOO!")
    else:
        led.off()
        buzzer.off()
        print("Zzzz")
    time.sleep(0.5)
