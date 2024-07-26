from datetime import datetime
import time

# This function prints a message based on whether the current time ends with an even or odd number
def solution1():
    # Get the current time as a formatted string (e.g., '2024-07-26T12:34:56')
    time_right_now = datetime.fromtimestamp(int(time.time())).isoformat()
    
    # Extract the last digit of the current time (this will be a string)
    last_digit = None  # <-- Fill this in
    
    # Convert the last digit to an integer
    last_digit_int = None  # <-- Fill this in
    
    # Check if the last digit is even or odd
    if None:  # <-- Fill this in
        # If the last digit is even, print this message
        print(f"The time: {time_right_now} ended with an even number! We're Even Stevens.")
    else:
        # If the last digit is odd, print this message
        print(f"The time: {time_right_now} ended with an odd number! No I'm not, you're odd.")
