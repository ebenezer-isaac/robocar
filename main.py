import pygame, sys
import pygame.locals
import RPi.GPIO as GPIO
from time import sleep
import picamera
import pygame
import io

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
wheel1_pwm.start(0)
wheel2_pwm.start(0)
wheel3_pwm.start(0)
wheel4_pwm.start(0)



pygame.init()
print("initialized")
screen = pygame.display.set_mode((320,240))

camera = picamera.PiCamera()
camera.rotation = 180
camera.resolution = (320, 240)
camera.crop = (0.0, 0.0, 1.0, 1.0)

x = (screen.get_width() - camera.resolution[0]) / 2
y = (screen.get_height() - camera.resolution[1]) / 2

rgb = bytearray(camera.resolution[0] * camera.resolution[1] * 3)

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
        print(speed)
    if keys[pygame.K_MINUS]:
    	if speed >1:
    		speed = speed - 1
        print(speed)
    if keys[pygame.K_w] and keys[pygame.K_a]:
    	direction = 0
    	wheel1_pwm.ChangeDutyCycle(20)
    	wheel2_pwm.ChangeDutyCycle(0)
    	wheel3_pwm.ChangeDutyCycle(100)
    	wheel4_pwm.ChangeDutyCycle(0)
    elif keys[pygame.K_w] and keys[pygame.K_d]:
    	direction = 0
    	wheel1_pwm.ChangeDutyCycle(100)
    	wheel2_pwm.ChangeDutyCycle(0)
    	wheel3_pwm.ChangeDutyCycle(20)
    	wheel4_pwm.ChangeDutyCycle(0)
    elif keys[pygame.K_s] and keys[pygame.K_a]:
    	direction = 0
    	wheel1_pwm.ChangeDutyCycle(0)
    	wheel2_pwm.ChangeDutyCycle(20)
    	wheel3_pwm.ChangeDutyCycle(0)
    	wheel4_pwm.ChangeDutyCycle(100)
    elif keys[pygame.K_s] and keys[pygame.K_d]:
    	direction = 0
    	wheel1_pwm.ChangeDutyCycle(0)
    	wheel2_pwm.ChangeDutyCycle(100)
    	wheel3_pwm.ChangeDutyCycle(0)
    	wheel4_pwm.ChangeDutyCycle(20)
    elif keys[pygame.K_w]:
    	direction = 0
    	wheel1_pwm.ChangeDutyCycle(100)
    	wheel2_pwm.ChangeDutyCycle(0)
    	wheel3_pwm.ChangeDutyCycle(100)
    	wheel4_pwm.ChangeDutyCycle(0)
    elif keys[pygame.K_s]:
    	direction = 1
    	wheel1_pwm.ChangeDutyCycle(0)
    	wheel2_pwm.ChangeDutyCycle(100)
    	wheel3_pwm.ChangeDutyCycle(0)
    	wheel4_pwm.ChangeDutyCycle(100)
    elif keys[pygame.K_a]:
    	if direction==0:
            wheel1_pwm.ChangeDutyCycle(0)
            wheel2_pwm.ChangeDutyCycle(0)
            wheel3_pwm.ChangeDutyCycle(100)
            wheel4_pwm.ChangeDutyCycle(0)
        elif direction==1:
            wheel1_pwm.ChangeDutyCycle(0)
            wheel2_pwm.ChangeDutyCycle(0)
            wheel3_pwm.ChangeDutyCycle(0)
            wheel4_pwm.ChangeDutyCycle(100)
    elif keys[pygame.K_d]:
    	if direction==0:
            wheel1_pwm.ChangeDutyCycle(100)
            wheel2_pwm.ChangeDutyCycle(0)
            wheel3_pwm.ChangeDutyCycle(0)
            wheel4_pwm.ChangeDutyCycle(0)
        elif direction==1:
            wheel1_pwm.ChangeDutyCycle(0)
            wheel2_pwm.ChangeDutyCycle(100)
            wheel3_pwm.ChangeDutyCycle(0)
            wheel4_pwm.ChangeDutyCycle(0)
    elif keys[pygame.K_SPACE]:
    	wheel1_pwm.ChangeDutyCycle(0)
    	wheel2_pwm.ChangeDutyCycle(0)
    	wheel3_pwm.ChangeDutyCycle(0)
    	wheel4_pwm.ChangeDutyCycle(0)
    else:
    	wheel1_pwm.ChangeDutyCycle(0)
    	wheel2_pwm.ChangeDutyCycle(0)
    	wheel3_pwm.ChangeDutyCycle(0)
    	wheel4_pwm.ChangeDutyCycle(0)
    stream = io.BytesIO()
    camera.capture(stream, use_video_port=True, format='rgb')
    stream.seek(0)
    stream.readinto(rgb)
    stream.close()
    img = pygame.image.frombuffer(rgb[0:
          (camera.resolution[0] * camera.resolution[1] * 3)],
           camera.resolution, 'RGB')
    screen.fill(0)
    if img:
        screen.blit(img, (x,y))
    pygame.display.update()
camera.close()
pygame.display.quit()
