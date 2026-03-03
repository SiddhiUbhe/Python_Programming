from functools import reduce

ChkString = lambda str : (len(str) > 5)

def main():
    Data = ["Python", "Programming", "Java", "Hello", "Failed"]
    print("Actual data is : ",Data)

    FData = list(filter(ChkString, Data))
    print("Data after filter string having length greater than 5 is : ",FData)

if __name__ == "__main__":
    main()    