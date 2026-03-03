from functools import reduce

Divisible = lambda No : (No % 3 == 0) and (No % 5 == 0)

def main():
    Data = [22,34,45,15,6]
    print("Actual data is : ",Data)

    FData = list(filter(Divisible,Data))
    print("Data after filter and divisbile by 3 and 5 is : ",FData)

if __name__ == "__main__":
    main()    