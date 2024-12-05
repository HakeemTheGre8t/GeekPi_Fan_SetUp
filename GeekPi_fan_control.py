import time
import psutil
import RPi.GPIO as GPIO



GPIO.setwarnings(False)  # Disable GPIO warnings



# Set up GPIO for fan control
FAN_PIN = 17  # GPIO pin for the fan
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)  # Set the pin as an output



# Define the temperature thresholds
TEMP_THRESHOLD_ON = 50.0  # Temperature above which the fan will turn on
TEMP_THRESHOLD_OFF = 40.0  # Temperature below which the fan will turn off



def get_cpu_temp():
    try:
        # Access the CPU temperature using 'cpu_thermal'
        return psutil.sensors_temperatures()['cpu_thermal'][0].current  # The sensor name in my case is 'cpu_thermal', so I updated the get_cpu_temp() function to access this sensor.
    except KeyError:
        print("Unable to read CPU temperature.")
        return 47.0  # Fallback value for simulation



def control_fan(temp):
    if temp >= TEMP_THRESHOLD_ON:
        print("Temperature exceeded threshold. Turning fan ON.")
        GPIO.output(FAN_PIN, GPIO.HIGH)  # Turn fan on
    elif temp <= TEMP_THRESHOLD_OFF:
        print("Temperature below threshold. Turning fan OFF.")
        GPIO.output(FAN_PIN, GPIO.LOW)  # Turn fan off



if __name__ == "__main__":
    while True:
        temp = get_cpu_temp()  # Get the current CPU temperature
        if temp:
            print(f"Current CPU temperature: {temp}°C")
            control_fan(temp)  # Control the fan based on the temperature
        time.sleep(5)  # Check the temperature every 5 seconds