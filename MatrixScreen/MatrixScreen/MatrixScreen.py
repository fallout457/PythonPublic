import random
import sys
import time

_characters=[" ","0","1"]


try:
    while True:
        _lettersToBeShown = ""
        x = 0
        y = random.randint(40,120)
        for a in range(x, y):
            _lettersToBeShown = _lettersToBeShown + _characters[random.randint(0,2)]
        
            
        print('\033[92m' + _lettersToBeShown)

except:
    print("\nQuiting...")
    sys.exit()
    