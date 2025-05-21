from machine import ADC, Pin, PWM
import time
time.sleep(0.1) # Wait for USB to become ready

pot = ADC(2)  # GP28
led = PWM(Pin(15))  # GP15
led.freq(1000)

while True:
    val = pot.read_u16()  # Valor de 0 a 65535
    duty = int(val / 256)  # Convertir a rango PWM (0-255 aprox)
    led.duty_u16(val)
    print("Brillo:", duty)
    time.sleep(0.05)
