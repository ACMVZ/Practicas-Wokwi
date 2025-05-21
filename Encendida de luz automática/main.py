from machine import ADC, Pin
import time

time.sleep(0.1) # Wait for USB to become ready

ldr = ADC(2)
led = Pin(10, Pin.OUT)

while True:
    luz = ldr.read_u16()
    if luz < 20000:
        led.on()
    else:
        led.off()
    time.sleep(0.5)
