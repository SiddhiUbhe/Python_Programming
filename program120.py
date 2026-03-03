from functools import reduce

MinimumNum = lambda No1, No2 : No1 if (No1 < No2) else No2

def main():
    Data = [22,34,45,5,6]
    print("Actual data is : ",Data)

    RData = reduce(MinimumNum, Data)
    print("Data after reduce is and minimum number is : ",RData)

if __name__ == "__main__":
    main()    