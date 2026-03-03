from functools import reduce

MaximumNum = lambda No1, No2 : No1 if(No1 > No2) else No2

def main():
    Data = [2,3,4,5,6]
    print("Actual data is : ",Data)

    RData = reduce(MaximumNum, Data)
    print("Data after reduce is and maximum number is : ",RData)

if __name__ == "__main__":
    main()