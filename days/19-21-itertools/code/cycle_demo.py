import itertools
import sys
import time
import random

lights = itertools.cycle(['green', 'yellow', 'red'])

while True:
    sys.stdout.write("\r" + next(lights))
    sys.stdout.flush()
    time.sleep(random.randint(3, 5)*10)
