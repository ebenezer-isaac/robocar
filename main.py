import RPi.GPIO as GPIO
from time import sleep # Import the sleep function from the time module
#GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.HIGH) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(10, GPIO.OUT, initial=GPIO.HIGH) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(16, GPIO.OUT, initial=GPIO.HIGH) # Set pin 8 to be an output pin and set initial value to low (off)

while True: # Run forever
 GPIO.output(8, GPIO.LOW)
 GPIO.output(10, GPIO.HIGH)
 GPIO.output(12, GPIO.LOW)
 GPIO.output(16, GPIO.HIGH)
 print("high")
 sleep(2)
 GPIO.output(8, GPIO.HIGH) # Turn off
 GPIO.output(10, GPIO.LOW) # Turn off
 GPIO.output(12, GPIO.HIGH) # Turn off
 GPIO.output(16, GPIO.LOW) # Turn off
 print("low")
 sleep(2) # Sleep for 1 second
 GPIO.output(8, GPIO.LOW) # Turn off
 GPIO.output(10, GPIO.LOW) # Turn off
 GPIO.output(12, GPIO.LOW) # Turn off
 GPIO.output(16, GPIO.LOW) # Turn off
 print("low")
 sleep(2) # Sleep for 1 second
