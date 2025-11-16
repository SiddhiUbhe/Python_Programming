'''
Given an integer n:
If n is odd, print "Weird"
If n is even and in the range 2 to 5, print "Not Weird"
If n is even and in the range 6 to 20, print "Weird"
If n is even and greater than 20, print "Not Weird"

Input: One positive integer n
Output: Print "Weird" or "Not Weird" based on the rules.
'''

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n in range(2, 6):  # 2 to 5
        print("Not Weird")
    elif n % 2 == 0 and n in range(6, 21):  # 6 to 20
        print("Weird")
    else:  # n > 20 and even
        print("Not Weird")