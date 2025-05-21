from machine import Pin
import time

time.sleep(0.1) # Wait for USB to become ready

pir = Pin(14, Pin.IN)

while True:
    if pir.value():
        print("¡Movimiento detectado!")
    else:
        print("Sin movimiento.")
    time.sleep(1)
