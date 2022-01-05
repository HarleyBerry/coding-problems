import random
import time

while True:
    pc=random.randrange(1,6)
    print(pc)
    if pc==1:
        print (2)
    elif pc==2:
        print (3)
    elif pc==3:
        print (4)
    elif pc==4:
        print (5)
    else :
        print ('error')
    time.sleep(1)
    
