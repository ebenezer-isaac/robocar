#sudo pigpiod
import pygame, sys
import pygame.locals
import RPi.GPIO as GPIO
from time import sleep
import picamera
import pygame
import io
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

panServoPin = 12 #BCM
tiltServoPin = 25 #BCM
factory = PiGPIOFactory()
panServo = Servo(panServoPin,min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
tiltServo = Servo(tiltServoPin,min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)


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
camera.resolution = (320, 240)
camera.crop = (0.0, 0.0, 1.0, 1.0)

panPosition = 0
tiltPosition = 0.5
panServo.mid()
tiltServo.value = tiltPosition
sleep(0.1)

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
    if keys[pygame.K_KP5]:
        panPosition = 0
        tiltPosition = 0.5
        tiltServo.value = tiltPosition
        panServo.mid()
        sleep(0.1)
    if keys[pygame.K_KP4]:
        if panPosition<1:
            panPosition = panPosition+0.03
        if panPosition>1:
            panPosition = 1
        panServo.value = panPosition
        sleep(0.001)
    if keys[pygame.K_KP6]:
        if panPosition>-1:
            panPosition = panPosition-0.03
        if panPosition<-1:
            panPosition = -1
        panServo.value = panPosition
        sleep(0.001)

    if keys[pygame.K_KP2]:
        if tiltPosition<1:
            tiltPosition = tiltPosition+0.03
        if tiltPosition>1:
            tiltPosition = 1
        tiltServo.value = tiltPosition
        sleep(0.001)
    if keys[pygame.K_KP8]:
        if tiltPosition>-1:
            tiltPosition = tiltPosition-0.03
        if tiltPosition<-1:
            tiltPosition = -1
        tiltServo.value = tiltPosition
        sleep(0.001)
    if keys[pygame.K_w] and keys[pygame.K_a]:
        direction = 0
        wheel1_pwm.ChangeDutyCycle(0)
        wheel2_pwm.ChangeDutyCycle(0)
        wheel3_pwm.ChangeDutyCycle(100)
        wheel4_pwm.ChangeDutyCycle(0)
    elif keys[pygame.K_w] and keys[pygame.K_d]:
        direction = 0
        wheel1_pwm.ChangeDutyCycle(100)
        wheel2_pwm.ChangeDutyCycle(0)
        wheel3_pwm.ChangeDutyCycle(0)
        wheel4_pwm.ChangeDutyCycle(0)
    elif keys[pygame.K_s] and keys[pygame.K_a]:
        direction = 0
        wheel1_pwm.ChangeDutyCycle(0)
        wheel2_pwm.ChangeDutyCycle(5)
        wheel3_pwm.ChangeDutyCycle(0)
        wheel4_pwm.ChangeDutyCycle(100)
    elif keys[pygame.K_s] and keys[pygame.K_d]:
        direction = 0
        wheel1_pwm.ChangeDutyCycle(0)
        wheel2_pwm.ChangeDutyCycle(100)
        wheel3_pwm.ChangeDutyCycle(0)
        wheel4_pwm.ChangeDutyCycle(5)
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
            wheel2_pwm.ChangeDutyCycle(100)
            wheel3_pwm.ChangeDutyCycle(100)
            wheel4_pwm.ChangeDutyCycle(0)
        elif direction==1:
            wheel1_pwm.ChangeDutyCycle(100)
            wheel2_pwm.ChangeDutyCycle(0)
            wheel3_pwm.ChangeDutyCycle(0)
            wheel4_pwm.ChangeDutyCycle(100)
    elif keys[pygame.K_d]:
        if direction==0:
            wheel1_pwm.ChangeDutyCycle(100)
            wheel2_pwm.ChangeDutyCycle(0)
            wheel3_pwm.ChangeDutyCycle(0)
            wheel4_pwm.ChangeDutyCycle(100)
        elif direction==1:
            wheel1_pwm.ChangeDutyCycle(0)
            wheel2_pwm.ChangeDutyCycle(100)
            wheel3_pwm.ChangeDutyCycle(100)
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
panServo.mid()
tiltServo.value = 0.5
sleep(0.1)
camera.close()
pygame.display.quit()
GPIO.cleanup()