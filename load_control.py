import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def control_load(led_pin=5):
    GPIO.setup(led_pin, GPIO.OUT)
    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(1800)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(1800)

if __name__ == "__main__":

    load_thread = threading.Thread(target=control_load)

    load_thread.start()

    load_thread.join()

    GPIO.cleanup()
