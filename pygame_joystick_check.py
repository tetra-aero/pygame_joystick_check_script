# https://www.oki-lab.net/entry/post-687

import pygame
from pygame.locals import *
import time
 
def main():
    pygame.init()
    joystick=pygame.joystick.Joystick(0)
    joystick.init()
    print("Joystick Name: " + joystick.get_name())
    print("Number of Button : " + str(joystick.get_numbuttons()))
    print("Number of Axis : " + str(joystick.get_numaxes()))
    print("Number of Hats : " + str(joystick.get_numhats()))
    
    time.sleep(0.5)
	
    try:
        while True:
            for e in pygame.event.get():
                if e.type==pygame.locals.JOYAXISMOTION:
                    a=[]
                    for i in range(4):
                        a.append(joystick.get_axis(i))
                    print("JOYSTICK:" + str(a))
                if e.type==pygame.locals.JOYBUTTONDOWN:
                    print ("BUTTON:" + str(e.button))
                if e.type==pygame.locals.JOYHATMOTION:
                    b,c = joystick.get_hat(0)
                    print ("HAT:" + str(b) + ", " + str(c))
				#pass
            time.sleep(0.1)
    except(KeyboardInterrupt):
        print("Close")
 
if __name__=="__main__":
    main()
