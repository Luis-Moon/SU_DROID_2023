#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.nxtdevices import *
from pybricks.parameters import *
from pybricks.tools import *
from pybricks.robotics import *
from pybricks.media.ev3dev import *


ev3 = EV3Brick()

import time
ev3 = EV3Brick()
crono = StopWatch()
vel = 160
motorL = Motor(Port.A)
motorR = Motor(Port.B)
# ultrassom = UltrasonicSensor(Port.S2)
# distFrente = ultrassom.distance()/10
sensorCorL = LightSensor(Port.S1)
sensorCorR = LightSensor(Port.S3)
botao = TouchSensor(Port.S4)
robo = DriveBase(motorL, motorR, wheel_diameter=42.5, axle_track=112)
corBrancaL = sensorCorL.reflection()
corBrancaR = sensorCorR.reflection()
def som(hz):
    ev3.speaker.beep(i)

def victori():
    for i in range(1200, 0, -100):
        ev3.speaker.beep(i)

def preto_dos_dois_lados():
    return (sensorCorL.reflection() <= 15) and (sensorCorR.reflection() <= 15)


def preto_dos_dois_lados():
    return (sensorCorL.reflection() <= 15) and (sensorCorR.reflection() <= 15)

def ver_preto_esquerda():
    return sensorCorL.reflection() <= 15


def ver_preto_direita():
    return sensorCorR.reflection() <= 15

def virar_direita(angulo):
    robo.turn(angulo)

def virar_esquerda(angulo):
    robo.turn(-angulo)


def seguir_reto(velocity):
    robo.drive(velocity, 0)


def parar():
    robo.stop()


robo.settings(100, 100, 3000 , 3000)