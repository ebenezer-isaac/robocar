import pygame, sys
import pygame.locals
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
wheel1_pwm = GPIO.PWM(8,1000)
wheel2_pwm = GPIO.PWM(10,1000)
wheel3_pwm = GPIO.PWM(12,1000)
wheel4_pwm = GPIO.PWM(16,1000)
wheel1_pwm.start(100)
wheel2_pwm.start(100)
wheel3_pwm.start(100)
wheel3_pwm.start(100)


pygame.init()
print("initialized")
screen = pygame.display.set_mode((200,200))
running = True
direction = 0
speed = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_PLUS]:
    	if speed <5:
    		speed = speed + 1
    if keys[pygame.K_MINUS]:
    	if speed >1:
    		speed = speed - 1
    if keys[pygame.K_w]:
    	direction = 0
    	wheel1_pwm.ChangeDutyCycle(100)
    	wheel2_pwm.ChangeDutyCycle(100-(speed*20))
    	wheel3_pwm.ChangeDutyCycle(100)
    	wheel4_pwm.ChangeDutyCycle(100-(speed*20))
#        GPIO.output(8, GPIO.HIGH)
#        GPIO.output(10, GPIO.LOW)
#        GPIO.output(12, GPIO.HIGH)
#        GPIO.output(16, GPIO.LOW)
    elif keys[pygame.K_s]:
    	direction = 1
        GPIO.output(8, GPIO.LOW)
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.HIGH)
    elif keys[pygame.K_a]:
    	if direction==0:
            GPIO.output(8, GPIO.LOW)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(12, GPIO.HIGH)
            GPIO.output(16, GPIO.LOW)
        elif direction==1:
            GPIO.output(8, GPIO.LOW)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(16, GPIO.HIGH)
    elif keys[pygame.K_d]:
    	if direction==0:
            GPIO.output(8, GPIO.HIGH)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(16, GPIO.LOW)
        elif direction==1:
            GPIO.output(8, GPIO.LOW)
            GPIO.output(10, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(16, GPIO.LOW)
    elif keys[pygame.K_SPACE]:
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
    else:
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)

