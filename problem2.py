#! python3
"""
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
(2 marks)

inputs:
int number

outputs:
multiples of that number on one line

example:
Enter a number: 4
4 8 12 16 20 24 28 32 36 40 44 48
"""

import math
import time

targetNum = 75
counter = 5
while True:
    print(counter, end ="", flush=True)
    counter = counter + 5
    # time.sleep(x) will pause the program at this point for x seconds where x is a float 
    time.sleep(0.25)
    if counter > 76:
       break
print("===================")