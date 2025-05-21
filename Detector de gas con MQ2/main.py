from machine import ADC
import time

time.sleep(0.1) # Wait for USB to become ready

mq2 = ADC(0)

while True:
    level = mq2.read_u16()
    print("Nivel de gas:", level)
    time.sleep(1)
