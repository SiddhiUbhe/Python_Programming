OddNum = lambda No : (No % 2 != 0)

def main():
    Data = [2,3,4,5,6]
    print("Actual data is : ",Data)

    FData = list(filter(OddNum, Data))
    print("Data after filter is : ", FData)

if __name__ == "__main__":
    main()    