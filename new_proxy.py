import RPi.GPIO as GPIO
import time
import json

def initialize_sensors(interrupt_pins):
    # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Global variables for each sensor
    pulses = [0] * len(interrupt_pins)
    last_times = [0] * len(interrupt_pins)
    pulses_per_revolution = 1

    def count_pulse(channel):
        nonlocal pulses, last_times

        sensor_index = interrupt_pins.index(channel)
        current_time = time.time() * 1000  # Convert seconds to milliseconds

        if current_time - last_times[sensor_index] >= 1000:
            rpm = (pulses[sensor_index] * 60.0) / ((current_time - last_times[sensor_index]) / 1000.0) / pulses_per_revolution

            sense_num = sensor_index + 1
            with open('data.json', 'r') as file:
                data = json.load(file)
            data[sense_num] = round(rpm, 2)
            with open('data.json', 'w') as file:
                json.dump(data, file)
            pulses[sensor_index] = 0
            last_times[sensor_index] = current_time

        pulses[sensor_index] += 1

    # Set up GPIO pins for input with pull-up resistors and add event detection
    for pin in interrupt_pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=count_pulse)

    return pulses

def get_sensor_values():
    interrupt_pins = [17, 23, 27, 18, 13]
    pulses = initialize_sensors(interrupt_pins)
    sensor_values = []

    try:
        print("Waiting for interrupts...")
        while True:
            # Assuming each sensor corresponds to an index in pulses
            sensor_values = pulses[:]
            time.sleep(1)

    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        GPIO.cleanup()
        print("\nProgram terminated by user.")

    return sensor_values

# Example usage:
sensor_values = get_sensor_values()
print("Sensor Values:", sensor_values)
