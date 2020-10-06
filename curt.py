from curtsies import Input
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(10, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(16, GPIO.OUT, initial=GPIO.HIGH)

with Input(keynames='curses') as input_generator:
    for key in input_generator:
        print(key)
        while key == 'w':
             GPIO.output(8, GPIO.LOW)
             GPIO.output(10, GPIO.HIGH)
             GPIO.output(12, GPIO.LOW)
             GPIO.output(16, GPIO.HIGH)
        while key == ' ':
             GPIO.output(8, GPIO.LOW)
             GPIO.output(10, GPIO.LOW)
             GPIO.output(12, GPIO.LOW)
             GPIO.output(16, GPIO.LOW)

