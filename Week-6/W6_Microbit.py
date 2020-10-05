from microbit import *
import random

hand = 0

brick = Image("00000:"
             "09990:"
             "09990:"
             "09990:"
             "00000")

scissor = Image("99009:"
             "99090:"
             "00900:"
             "99090:"
             "99009")

paper = Image("99999:"
             "90009:"
             "90009:"
             "90009:"
             "99999")

egg = Image("00900:"
             "09990:"
             "99999:"
             "99999:"
             "09990")


hand = random.randint(0, 101)




while True:
    gesture = accelerometer.current_gesture()

    if gesture == "shake":
        if (hand > 0 and hand < 34):
            display.show(brick)
        
        elif (hand > 33 and hand < 67):
            display.show(scissor)
        
        elif (hand > 66 and hand < 99):
            display.show(paper)
        
        else:
            display.show(egg)
            
            
            
            
            