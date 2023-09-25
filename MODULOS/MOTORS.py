#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.nxtdevices import *
from pybricks.parameters import *
from pybricks.tools import *
from pybricks.robotics import *
from pybricks.media.ev3dev import *




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
LIDO = False
corBrancaL = sensorCorL.reflection()
corBrancaR = sensorCorR.reflection()


def straight(velocity):
    if (sensorCorL.reflection() <= 15) and (sensorCorR.reflection() <= 15):
        robo.stop()
        wait(500)
        robo.turn(-12)
    elif sensorCorL.reflection() <= 15:
        robo.stop()
        wait(500)
        robo.turn(-12)
    elif sensorCorR.reflection() <= 15:
        robo.stop()
        wait(500)
        robo.turn(12)
    else:
        robo.drive(50,0)
