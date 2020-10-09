import pygame, sys
import pygame.locals
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(10, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(16, GPIO.OUT, initial=GPIO.HIGH)

pygame.init()
print("initialized")
screen = pygame.display.set_mode((500,400))
running = True
direction = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
    	direction = 0
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
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
            GPIO.output(10, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(16, GPIO.LOW)
    elif keys[pygame.K_d]:
    	if direction==0:
            GPIO.output(8, GPIO.HIGH)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(16, GPIO.LOW)
        elif direction==1:
            GPIO.output(8, GPIO.LOW)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(16, GPIO.HIGH)
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

