# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:24:11 2019

@author: sunghwan
"""
from time import sleep
import tellopy

global_drone = tellopy.Tello()

def handler(event, sender, data, **args):
    global_drone = sender
    if event is global_drone.EVENT_FLIGHT_DATA:
        print(data)

def connectDrone():
    try:
        global_drone.subscribe(global_drone.EVENT_FLIGHT_DATA, handler)
        global_drone.connect() 
        global_drone.wait_for_connection(60.0)
        print('드론 접속 완료')
    except Exception as ex:
        print(ex)

def takeOffDrone():
    try:
        global_drone.takeoff()
    except Exception as ex:
        print(ex)

def landDrone():
   try:
        global_drone.land()
   except Exception as ex:
        print(ex)     
        
def quitDrone():
    global_drone.quit()        
        
def mainFlight():
    try:
        connectDrone()
        sleep(5)
        takeOffDrone()
        sleep(5)
        global_drone.land()
        sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        global_drone.quit()

if __name__ == '__main__':
    mainFlight()