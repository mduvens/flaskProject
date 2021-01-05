import numpy as np 

import threading
import random
import time



def getRandom():
    x = random.randint(0,9)
    return x

def getRandomAxis():
    x = [getRandom() for i in range(5)]
    y = [getRandom() for i in range(5)]
    return [x,y]




