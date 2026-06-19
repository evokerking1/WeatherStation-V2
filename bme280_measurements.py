import bme280
import smbus2
from time import sleep

from smbus2.smbus2 import SMBus

port = 1
address = 0x77
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus, address)

"""while True:
    bme280_data = bme280.sample(bus, address)
    humidity = bme280_data.humidity
    pressure = bme280_data.pressure
    ambient_temperature = bme280_data.temperature

    print(f"Humidity: {humidity}, Pressure: {pressure}, Ambient Temperature: {ambient_temperature}")

    sleep(1)"""


def read_all(bus: SMBus, address: int):
    bme280_data = bme280.sample(bus, address)

    return bme280_data.humidity, bme280_data.pressure, bme280_data.temperature

def read_humidity(bus: SMBus, address: int):
    bme280_data = bme280.sample(bus, address)

    return bme280_data.humidity

def read_pressure(bus: SMBus, address: int):
    bme280_data = bme280.sample(bus, address)

    return bme280_data.pressure

def read_temperature(bus: SMBus, address: int):
    bme280_data = bme280.sample(bus, address)

    return bme280_data.temperature