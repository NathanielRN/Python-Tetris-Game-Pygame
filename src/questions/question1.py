from datetime import datetime
import time

# Printing to the console + IF Statements

def solution1():
    time_right_now = datetime.fromtimestamp(int(time.time())).isoformat()
    
    if int(time_right_now[-1]) % 2 == 0:
        print("The time ended with an even number! We're Event Stevens.")
    else:
        print("The time ended with an odd number! No I'm not, you're odd.")
