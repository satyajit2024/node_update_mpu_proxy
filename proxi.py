import RPi.GPIO as GPIO
import time
import json

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for interrupts
interrupt_pins = [17,23,27,18,13 ]

# Global variables for each sensor
pulses = [0] * 5
last_times = [0] * 5
pulses_per_revolution = 1

def count_pulse(channel):
    global pulses, last_times

    sensor_index = interrupt_pins.index(channel)
    current_time = time.time() * 1000  # Convert seconds to milliseconds

    if current_time - last_times[sensor_index] >= 1000:
        rpm = (pulses[sensor_index] * 60.0) / ((current_time - last_times[sensor_index]) / 1000.0) / pulses_per_revolution

        print(f"Sensor {sensor_index + 1} RPM: {round(rpm,2)}")
        sense_num = sensor_index + 1
        with open ('data.json','r') as file:
            data = json.load(file)
        data[sense_num] = round(rpm,2)
        with open('data.json','w') as file:
            json.dump(data,file)
        pulses[sensor_index] = 0
        last_times[sensor_index] = current_time

    pulses[sensor_index] += 1
    #time.sleep(0.1)

# Set up GPIO pins for input with pull-up resistors and add event detection
# for pin in interrupt_pins:
#     GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#     GPIO.add_event_detect(pin, GPIO.FALLING, callback=count_pulse)

# try:
#     print("Waiting for interrupts...")
#     # while True:
#     time.sleep(10)

# except KeyboardInterrupt:
#     # Handle keyboard interrupt (Ctrl+C)
#     GPIO.cleanup()
#     print("\nProgram terminated by user.")

count_pulse(17)
count_pulse(23)
count_pulse(27)
count_pulse(18)

count_pulse(17)
count_pulse(23)
count_pulse(27)
count_pulse(18)