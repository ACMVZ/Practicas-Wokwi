import dht
from machine import Pin
import time

time.sleep(0.1) # Wait for USB to become ready

sensor = dht.DHT22(Pin(15))

while True:
    sensor.measure()
    print("Temp:", sensor.temperature(), "°C | Hum:", sensor.humidity(), "%")
    time.sleep(2)
