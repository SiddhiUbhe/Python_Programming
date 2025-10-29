# Read an integer n from input and print the square of all non-negative integers less than n.

# Input: 5
# Output:
# 0
# 1
# 4
# 9
# 16

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i**2)