# Given a year, determine whether it is a leap year.
# A leap year:
# - is divisible by 4, but not by 100, unless it is also divisible by 400.
# Return True if leap year, otherwise False.

def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False

    return leap

year = int(input())
print(is_leap(year))