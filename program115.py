SquareNum = lambda No: No**2

def main():
    Data = [2,3,4,5,6]
    print("Actual data is: ",Data)

    MData = list(map(SquareNum, Data)) 
    # map() is a built-in function
    # It applies a function to every element in a list
    # map(function, iterable)
    
    print("Data after map is: ",MData)

if __name__ == "__main__":
    main()
