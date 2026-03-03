from functools import reduce

Multiplication = lambda No1, No2 : No1 * No2

def main():
    Data = [2,4,4,5,1]
    print("Actual data is : ",Data)

    RData = reduce(Multiplication,Data)
    print("Data after reduce and product of all number is : ",RData)

if __name__ == "__main__":
    main()    