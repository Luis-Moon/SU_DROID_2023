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
corBrancaL = (sensorCorL.reflection() + corBrancaL) / 2
corBrancaR = (sensorCorR.reflection() + corBrancaR) / 2


def Choose():
    crono.reset()
    pressionado = False
    while crono.time() < 5000:
        if botao.pressed():
            pressionado = True
            break
    if pressionado:
        time.sleep(1)
        robo.straight(80)
        robo.turn(-90)
        robo.straight(100)
        robo.turn(90)
        vel = 90
    else:
        robo.straight(80)
        robo.turn(90)
        robo.straight(20)


def Verde(LIDO):
    if (LIDO):
        return sensorCorL.reflection() in range(10,96)
    return False


def finished():
    LIDO = sensorCorL.reflection() in range(10,96)
    return sensorCorL.reflection() in range(10,96)


def andarParaFrente():
    while (finished() == False or Verde(LIDO)):
        distFrente = ultrassom.distance()/10
        robo.drive(vel, 0)
        if distFrente <= 5 and LIDO == False:
            time.sleep(0.05)
            desviarObstaculo()
        elif (sensorCorL.reflection() < corBrancaL * 0.75) and (sensorCorR.reflection() < corBrancaR * 0.75):
            pass
        elif sensorCorL.reflection() < corBrancaL * 0.75:
            robo.stop()
            while sensorCorL.reflection() < corBrancaL * 0.75:
                robo.drive(0, -60)
                if sensorCorR.reflection() < corBrancaR * 0.75:
                    break
            robo.stop()
        elif sensorCorR.reflection() < corBrancaR * 0.75:
            robo.stop()
            while sensorCorR.reflection() < corBrancaR * 0.75:
                robo.drive(0, 60)
                if sensorCorL.reflection() < corBrancaL * 0.75:
                    break
            robo.stop()
    robo.stop()


def desviarObstaculo():
    robo.stop()
    robo.settings(300, 500, 360, 500)
    robo.turn(90)
    robo.stop()
    robo.straight(200)
    robo.stop()
    robo.turn(-90)
    robo.stop()
    robo.straight(340)
    robo.stop()
    robo.turn(-90)
    robo.stop()
    robo.straight(200)
    robo.stop()
    robo.turn(90)
    robo.stop()
