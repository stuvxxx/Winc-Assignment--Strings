# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

import time
import zen
import math
import datetime

def wait(seconds):
    time.sleep(seconds)

def my_sin(float):
    return math.sin(float)

def iso_now():
    print(datetime.now().strftime("%Y-%m-%dT%H:%M"))


iso_now()

