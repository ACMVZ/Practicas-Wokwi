from machine import ADC
from math import log
import time

time.sleep(0.1) # Wait for USB to become ready

# Configura el pin ADC
adc = ADC(26)  # GP26 en Pico W

# Constantes del NTC
BETA = 3950         # Coeficiente Beta
R0 = 10000          # Resistencia a 25°C
T0 = 298.15         # 25°C en Kelvin
VCC = 3.3           # Voltaje de referencia
R_SERIES = 10000    # Resistencia en serie con el NTC

def read_temperature():
    # Leer valor ADC (12 bits en Pico → rango 0-4095)
    adc_value = adc.read_u16() >> 4  # Escalado a 0-4095
    voltage = (adc_value / 4095) * VCC

    # Convertir a resistencia del NTC
    if voltage == 0:
        return None  # evitar división por cero
    r_ntc = R_SERIES * (VCC / voltage - 1)

    # Calcular temperatura en Kelvin y luego Celsius
    temperature_k = 1 / (1/T0 + (1/BETA) * log(r_ntc / R0))
    temperature_c = temperature_k - 273.15
    return temperature_c

while True:
    temp = read_temperature()
    if temp is not None:
        print("Temperatura: {:.2f} °C".format(temp))
    else:
        print("Error leyendo el sensor")
    time.sleep(1)
