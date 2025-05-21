from machine import ADC
import time
time.sleep(0.1) # Wait for USB to become ready

ldr = ADC(2)  # GP28

while True:
    luz = ldr.read_u16()
    print("Luz:", luz)
    time.sleep(1)
