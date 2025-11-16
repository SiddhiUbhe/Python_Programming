"""
Task:
Given an integer n, print the numbers from 1 to n consecutively without spaces.

Example:
Input: 3
Output: 123

The program reads an integer from STDIN and prints the sequence 1 to n 
as a continuous string, without using any string methods.
"""

if __name__ == '__main__':
    n = int(input())
    
    for i in range(1, n+1):
        print(i, end="")