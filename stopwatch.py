#Write a Python program to create a simple stopwatch using time module.

import time

def stopwatch():
    print("Press Enter to start/stop the stopwatch")
    
    while True:
        input("Press Enter to start")
        start=time.time()
        print("Stopwatch running...")
        
        input("Press Enter again to stop")
        end=time.time()
        
        duration = end - start
        
        print("Stopwatch time is : ",int(duration),"seconds" )
    
stopwatch()
    
    