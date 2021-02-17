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

targetNum = 48
count = 4

print("===================")
while targetNum == 48:
    print(count)
    count = count + 4
    # time.sleep(x) will pause the program at this point for x seconds where x is a float 
    time.sleep(0.25)
    if count > 48:
        break
print("===================")