import dht
from machine import Pin
import time

time.sleep(0.1) # Wait for USB to become ready

sensor = dht.DHT22(Pin(15))
led = Pin(14, Pin.OUT)

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    
    print("Temperatura:", temp, "°C - Humedad:", hum, "%")
    
    if temp > 30:
        led.on()
    else:
        led.off()
    
    time.sleep(2)
