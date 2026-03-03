from functools import reduce

Add = lambda No1, No2 : No1 + No2

def main():
    Data = [2,3,4,5,6]
    print("Actual data is : ",Data)

    RData = reduce(Add, Data)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()    