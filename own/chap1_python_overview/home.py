"""
Module and Import

Look at using_my_home.py together
"""

from time import ctime

class MyHome:
    colorRoof = 'red'
    stateDoor = 'closed'

    def paintRoof(self, color):
        self.colorRoof = color
    def openDoor(self):
        self.stateDoor = 'open'
    def closeDoor(self):
        self.stateDoor = 'close'
    def printStatus(self):
        print("Door color is", self.colorRoof, \
            ", and door is", self.stateDoor)
    
    def __init__(self, strAddress):
        print("Built on", strAddress)
        print("Built at", ctime())
    def __del__(self):
        print("Destroyed at", ctime())