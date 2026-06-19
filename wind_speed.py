from gpiozero import Button
import time
import math
import statistics

store_speeds = [] # Store the last 5 wind speeds to calculate an average


wind_count: int = 0 # Counts how many half rotations
radius: float = 9.0 # Radius of the anemometer in cm
wind_interval: int = 5 # how often (secs) to report the wind speed

CM_IN_A_KM = 100000.0
SECS_IN_AN_HOUR = 3600

# Every half rotation of the anemometer, increase the count by 1
def spin():
    global wind_count

    wind_count = wind_count + 1
    # print("spin" + str(windcount))

# Calculate the wind speed every wind_interval seconds
def calculate_speed(time_sec):
    global wind_count
    circumference_cm = (2 * math.pi) * radius
    rotations = wind_count / 2.0

    dist_km = (circumference_cm * rotations) / CM_IN_A_KM

    km_per_sec = dist_km / time_sec
    km_per_hour = km_per_sec * SECS_IN_AN_HOUR

    return km_per_hour

wind_speed_sensor = Button(5)
wind_speed_sensor.when_pressed = spin()

def reset_wind():
    global wind_count
    wind_count = 0

while True:
    wind_count = 0
    time.sleep(wind_interval)
    start_time = time.time()
    while time.time() - start_time <= wind_interval:
        reset_wind()
        time.sleep(wind_interval)
        final_speed = calculate_speed(wind_interval)
        store_speeds.append(final_speed)

    wind_gust = max(store_speeds)
    wind_speed = statistics.mean(store_speeds)
    print(wind_speed, wind_gust)